## 钱包生成器 README

### 简介
批量生成 Web3 EVM(以太坊系)钱包，输出地址与助记词到 CSV，便于导入钱包或归档管理。

### 功能
- 批量生成地址与助记词（BIP39）
- 标准派生路径 `m/44'/60'/0'/0/0`
- CSV 输出（UTF-8 with BOM），适配 Windows/Excel

### 环境要求
- Python 3.12.9（推荐）
- 系统：Windows/macOS/Linux
- 依赖：`eth-account`



### 创建虚拟环境（推荐）
创建并激活虚拟环境：
```bash
python3 -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```



### 安装
```bash
pip install -r requirements.txt
```



### 使用
- 默认（生成 10 个，自动生成带时间戳的文件名）：
```bash
python generate_wallets.py
```
- 指定数量：
```bash
python generate_wallets.py --count 100
# 或
python generate_wallets.py -n 100
```
- 指定输出文件：
```bash
python generate_wallets.py --out wallets.csv
# 或
python generate_wallets.py -o "C:\Users\blues\Documents\wallets.csv"
```
- 生成 12 词助记词：
```bash
python generate_wallets.py -n 10 --words 12 -o wallets_24.csv
```

### 参数
- `--count, -n`: 生成钱包数量（默认 10）
- `--out, -o`: 输出 CSV 文件路径（默认 `wallets_YYYYMMDD_HHMMSS.csv`）
- `--words`: 助记词词数，`12` 或 `24`（默认 24）

### 输出说明
- 编码：`utf-8-sig`
- 字段：
  - `index`: 序号（从 1 开始）
  - `address`: 0x 开头的 EVM 地址
  - `mnemonic`: BIP39 助记词（12 或 24 词）
- 示例：
```csv
index,address,mnemonic
1,0xAbC...,word1 word2 ... word12
```

### 钱包与派生路径
- 助记词标准：BIP39（英文词表）
- 派生路径：`m/44'/60'/0'/0/0`（Ethereum 标准）
- 需要第 N 个账户地址：将 `account_path` 改为 `m/44'/60'/0'/0/N`

### 安全提示
- 助记词 = 资产所有权，务必离线加密保存，不要上传云端或泄露。
- 在干净环境运行，避免恶意软件与剪贴板木马。
- 建议分离保存：地址可公开，助记词严格保密。

### 常见问题
- 如何生成 12 词助记词？
  - 运行时添加参数：`--words 12`
- 导入到钱包（如 MetaMask）：
  - 选择“从助记词导入”，粘贴助记词。
- CSV 乱码：
  - Excel 直接打开或选择 UTF-8（脚本已写入 BOM）。

### 故障排查
- 找不到依赖：
```bash
pip install -r requirements.txt
```
- 无法写入文件：检查路径权限或使用绝对路径。
- Windows 执行问题：可使用 `py generate_wallets.py` 运行。


### 免责声明
本工具仅用于学习与测试。请自行承担使用风险并遵守当地法律法规。 

