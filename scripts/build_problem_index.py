#!/usr/bin/env python3
"""Build a copyright-safe NUEDC problem metadata index from public file lists."""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote


CATEGORY_RULES: dict[str, tuple[str, ...]] = {
    "power-electronics": (
        "电源", "变换", "逆变", "整流", "充电", "电能", "功率", "负载", "发电",
        "稳压", "滤波", "回馈", "微电网", "无线充电", "电流源", "并网",
    ),
    "analog-rf": (
        "放大器", "振荡", "调制", "解调", "射频", "收音", "接收机", "频谱",
        "锁定", "均衡", "失真", "滤波器", "音频", "信号发生", "信号源",
    ),
    "instrumentation": (
        "测量", "测试仪", "分析仪", "示波", "频率计", "参数", "电阻", "电容",
        "电感", "电子秤", "检测", "电压表", "逻辑分析", "波形采集", "探测仪",
        "多用表", "有效值", "计数",
    ),
    "control-robotics": (
        "小车", "飞行器", "机器人", "摆", "控制", "泊车", "悬浮", "电机",
        "循迹", "跟踪", "瞄准", "巡查", "分拣", "货架", "打靶", "跷跷板",
        "运动装置", "帆板", "风板", "滚球", "送货", "送药", "汽车", "电动车",
        "小汽车", "温控", "水温控制",
    ),
    "communications-network": (
        "无线", "通信", "传输", "收发", "以太网", "光通信", "可见光", "网络",
        "定位", "遥控", "呼叫", "话筒", "同步时钟", "电缆", "双绞线",
    ),
    "sensing-vision-ai": (
        "视觉", "识别", "声源", "声音", "红外", "温度", "尺寸", "图像", "手势",
        "辨音", "摄像", "纸张", "液体", "目标物", "自动瞄准", "监控", "导引", "监测",
    ),
    "digital-systems-fpga": (
        "逻辑", "时序", "存储与回放", "点阵", "LED线阵", "数字信号", "ADC",
        "数字式", "波形存储", "数据采集", "芯片盒", "三子棋", "汉诺塔",
    ),
    "biomedical-environmental": (
        "脉搏", "植保", "环境", "水情", "消防", "动物", "路灯", "照明", "点滴",
        "体温", "药", "野生", "容器监控",
    ),
}

HARDWARE_RULES: dict[str, tuple[str, ...]] = {
    "power-stage": ("电源", "变换", "逆变", "整流", "充电", "负载", "回馈", "并网"),
    "precision-analog": ("测量", "测试仪", "电子秤", "电阻", "电容", "电感", "电压表"),
    "high-speed-sampling": ("示波", "频谱", "调制", "波形", "高速", "射频", "以太网"),
    "motor-drive": ("小车", "飞行器", "电机", "摆", "悬浮", "机器人", "分拣", "瞄准"),
    "vision-compute": ("视觉", "图像", "摄像", "识别", "目标物", "手势", "巡查"),
    "rf-front-end": ("射频", "无线", "收音", "接收机", "调幅", "调频", "通信"),
    "network-phy": ("以太网", "双绞线", "互联网", "网络"),
    "audio-chain": ("声音", "声源", "音频", "语音", "辨音", "话筒", "录音"),
    "mechanical-system": ("小车", "飞行器", "摆", "滚球", "悬浮", "机器人", "货架", "分拣"),
}

EXCLUDE_MARKERS = (
    "器件清单", "元器件清单", "题目列表", "历年题目", "Exams-list", "答疑统计",
    "附件", "附图", "数字字模", "总体图", "地貌图",
)

TITLE_ALIASES = {
    "易照明线路探测仪": "简易照明线路探测仪",
}


@dataclass(frozen=True)
class Problem:
    year: int
    event: str
    code: str
    title: str
    categories: tuple[str, ...]
    hardware_hints: tuple[str, ...]
    source: str
    source_path: str
    source_url: str


def normalize_title(value: str) -> str:
    value = value.replace("＿", "_").replace("－", "-")
    value = re.sub(r"^[题._\-\s]+", "", value)
    value = re.sub(r"[_\s]+", " ", value)
    return value.strip(" ._-")


def classify(title: str, rules: dict[str, tuple[str, ...]], fallback: str) -> tuple[str, ...]:
    tags = [name for name, keywords in rules.items() if any(word.lower() in title.lower() for word in keywords)]
    return tuple(tags or [fallback])


def parse_problem_path(raw_path: str, source: str) -> Problem | None:
    normalized_path = raw_path.replace("\\", "/").strip()
    suffix = Path(normalized_path).suffix.lower()
    if suffix not in {".pdf", ".doc", ".docx"}:
        return None
    if any(marker.lower() in normalized_path.lower() for marker in EXCLUDE_MARKERS):
        return None

    year_match = re.search(r"(?<!\d)((?:19|20)\d{2})(?!\d)", normalized_path)
    if not year_match:
        return None
    year = int(year_match.group(1))
    if not 1994 <= year <= 2026:
        return None

    stem = Path(normalized_path).stem
    stem = re.sub(rf"^{year}", "", stem).lstrip("_-/ ")
    code_match = re.match(r"^(?:题)?([A-Z])(?:题)?[._\-\s]*(.*)$", stem)
    code = ""
    title = stem
    if code_match:
        code = code_match.group(1)
        title = code_match.group(2)
    title = normalize_title(title)
    title = TITLE_ALIASES.get(title, title)
    if not title or title.isdigit():
        return None

    if "吉林" in normalized_path:
        event = "regional-jilin"
    elif any(token in normalized_path for token in ("省赛", "区域")):
        event = "regional"
    elif "2022/7月" in normalized_path:
        event = "national-july"
    elif "2022/10月" in normalized_path:
        event = "national-october"
    else:
        event = "national"
    if source == "nuedc-topic":
        url = "https://github.com/CCBP/NUEDC_Topic/blob/main/" + quote(normalized_path, safe="/")
    else:
        url = "https://github.com/chenshuo/nuedc/blob/main/docs/problems/" + quote(Path(normalized_path).name)

    return Problem(
        year=year,
        event=event,
        code=code,
        title=title,
        categories=classify(title, CATEGORY_RULES, "integrated-system"),
        hardware_hints=classify(title, HARDWARE_RULES, "general-embedded"),
        source=source,
        source_path=normalized_path,
        source_url=url,
    )


def collect(tree_file: Path | None, corpus_dir: Path | None) -> list[Problem]:
    candidates: list[tuple[str, str]] = []
    if tree_file:
        for line in tree_file.read_text(encoding="utf-8-sig").splitlines():
            if line.strip():
                candidates.append((line.strip(), "nuedc-topic"))
    if corpus_dir:
        for path in sorted(corpus_dir.rglob("*")):
            if path.is_file():
                candidates.append((path.name, "chenshuo-nuedc"))

    deduplicated: dict[tuple[int, str, str, str], Problem] = {}
    for raw_path, source in candidates:
        problem = parse_problem_path(raw_path, source)
        if not problem:
            continue
        key = (problem.year, problem.event, problem.code, re.sub(r"\W", "", problem.title).lower())
        previous = deduplicated.get(key)
        if previous is None or source == "nuedc-topic":
            deduplicated[key] = problem
    return sorted(deduplicated.values(), key=lambda item: (item.year, item.event, item.code, item.title))


def write_csv(problems: list[Problem], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    fields = ["year", "event", "code", "title", "categories", "hardware_hints", "source", "source_path", "source_url"]
    with output.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for item in problems:
            writer.writerow({
                "year": item.year,
                "event": item.event,
                "code": item.code,
                "title": item.title,
                "categories": ";".join(item.categories),
                "hardware_hints": ";".join(item.hardware_hints),
                "source": item.source,
                "source_path": item.source_path,
                "source_url": item.source_url,
            })


def write_summary(problems: list[Problem], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    category_counts = Counter(tag for item in problems for tag in item.categories)
    hardware_counts = Counter(tag for item in problems for tag in item.hardware_hints)
    year_counts = Counter(item.year for item in problems)
    lines = [
        "# Historical Problem Summary",
        "",
        f"Indexed problem records: **{len(problems)}**.",
        "",
        "> This file contains derived metadata only. Original problem documents are not redistributed.",
        "",
        "## Category Counts",
        "",
        "| Category | Records |",
        "|---|---:|",
    ]
    lines.extend(f"| `{name}` | {count} |" for name, count in category_counts.most_common())
    lines.extend(["", "## Hardware Hints", "", "| Hint | Records |", "|---|---:|"])
    lines.extend(f"| `{name}` | {count} |" for name, count in hardware_counts.most_common())
    lines.extend(["", "## Coverage by Year", "", "| Year | Records |", "|---:|---:|"])
    lines.extend(f"| {year} | {year_counts[year]} |" for year in sorted(year_counts))
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tree-file", type=Path, help="UTF-8 file containing repository paths, one per line")
    parser.add_argument("--corpus-dir", type=Path, help="Directory containing historical problem files")
    parser.add_argument("--out-csv", type=Path, default=Path("data/historical-problems.csv"))
    parser.add_argument("--out-summary", type=Path, default=Path("data/historical-summary.md"))
    parser.add_argument("--min-records", type=int, default=100)
    args = parser.parse_args()
    if not args.tree_file and not args.corpus_dir:
        parser.error("provide --tree-file, --corpus-dir, or both")
    problems = collect(args.tree_file, args.corpus_dir)
    if len(problems) < args.min_records:
        raise SystemExit(f"only {len(problems)} records found; expected at least {args.min_records}")
    write_csv(problems, args.out_csv)
    write_summary(problems, args.out_summary)
    print(f"wrote {len(problems)} records to {args.out_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
