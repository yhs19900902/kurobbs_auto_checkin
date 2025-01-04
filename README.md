# 库街区Auto Sign Job

这是一个自动签到任务的 GitHub Actions 工作流，旨在帮助用户通过定时任务自动执行库街区签到操作。通过使用 GitHub Actions，你可以在每天指定的时间自动运行签到脚本，而无需手动操作。

## 如何使用

### 1. Fork 仓库

首先，点击右上角的 `Fork` 按钮，将这个仓库 Fork 到你自己的 GitHub 账户下。

### 2. 设置 GitHub Secrets

为了确保签到脚本能够正常运行，你需要将必要的敏感信息（[token 获取教程](https://blog.tomys.top/2023-07/kuro-token/)）存储在 GitHub Secrets 中。

1. 进入你 Fork 后的仓库页面。
2. 点击 `Settings` 选项卡。
3. 在左侧菜单中选择 `Secrets and variables` > `Actions`。
4. 点击 `New repository secret` 按钮。
5. 在 `Name` 字段中输入 `TOKEN`，在 `Value` 字段中输入你的签到脚本所需的 token。
6. 点击 `Add secret` 保存。

### 3. 修改脚本（可选）

如果你需要修改签到脚本的逻辑，可以编辑 `auto_sign.py` 文件。确保脚本能够正确处理传入的 `TOKEN` 参数。

### 4. 触发工作流

#### 自动触发

工作流已经配置为每天北京时间早上 6 点（UTC 时间 22:00）自动运行。你无需手动操作，只需确保仓库中的代码和 Secrets 配置正确即可。

#### 手动触发

如果你想立即运行工作流，可以手动触发：

1. 进入你 Fork 后的仓库页面。
2. 点击 `Actions` 选项卡。
3. 在左侧菜单中选择 `Auto Sign Job`。
4. 点击右上角的 `Run workflow` 按钮，选择 `Run workflow` 即可手动触发。

### 5. 查看运行结果

每次工作流运行后，你可以在 `Actions` 选项卡中查看运行结果。如果签到成功，你应该能够看到相应的日志输出。

## 依赖

- Python 3.10
- 依赖库（如果有）可以在 `requirements.txt` 中列出，工作流会自动安装。

## 注意事项

- 确保 `TOKEN` 的安全性，不要将其直接写在代码中。
- 如果需要修改定时任务的执行时间，可以编辑 `.github/workflows/auto_sign.yml` 文件中的 `cron` 表达式。

## 特别感谢
本项目的签到脚本部分参考了 [TomyJan-API-Collection](https://github.com/TomyJan/Kuro-API-Collection) 的 API 实现。感谢 TomyJan 的开源贡献

## 贡献
如果你有任何改进建议或发现问题，欢迎提交 Issue 或 Pull Request.