# Day 01 — Typed Python Domain Model

## 今天完成的功能

- 使用 dataclass 建立职位、技能要求和候选人模型
- 使用 StrEnum 表示 required 和 preferred
- 对技能名称执行 strip 和 casefold 标准化
- 使用集合计算 matched 和 missing
- 从 JSON 加载职位和候选人数据
- 建立命令行入口
- 使用 pytest 覆盖领域模型、匹配算法和 CLI

## 遇到的真实错误

### Pyright 报告 reportUnknownVariableType

错误出现在 cli.py 的 require_object 函数。

虽然 isinstance(value, dict) 能确认 value 是字典，
但严格模式下 Pyright 仍然只知道它是
dict[Unknown, Unknown]，因此无法确认 key 的类型。

修复方法是先转换为 dict[object, object]，
检查所有 key 都是 str，再转换为 dict[str, object]。

## 另一个 Git 问题

多个文件显示为 AM。

原因是我先暂存了空文件，之后才在工作区写入代码。
暂存区保存的仍然是空文件版本。

通过 git restore --staged 取消暂存，
再按照功能重新 git add，避免提交错误版本。

## Java/Go 对照

- dataclass 类似 Java record 或 Go struct
- frozen=True 表示对象创建后不能重新赋值
- slots=True 减少动态属性并降低对象开销
- tuple 和 frozenset 用来表达不可变集合
- pytest fixture 类似测试框架提供的上下文对象

## 明天继续

- 使用 FastAPI 暴露职位匹配接口
- 学习 Pydantic request/response model
- 使用 TestClient 测试 HTTP API