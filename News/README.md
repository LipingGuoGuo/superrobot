### 今日头条爬虫说明
#### 调用的库
- 1、openpyxl
```
from openpyxl import Workbook
wb = Workbook()
# 新建的工作簿默认预先建好一个工作表，通过 active 属性获取
# 如果工作簿包含多个工作表，该属性将返回第一个
ws = wb.active

# 通过create_sheet建立新的工作表
ws1 = wb.create_sheet("Mysheet")
# 在前面插入新的工作表
ws2 = wb.create_sheet("Mysheet2",0)

# 命名表格名
ws.title = "New Title"

# 遍历所有工作表，直接for in更为优雅
for sheet in wb:
    print(sheet.titlt)

```
