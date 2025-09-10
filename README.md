#  Python（FastAPI + SQLite） & Java（Spring Boot + MySQL）

---

##  專案架構簡介（MVC 概念）

本專案遵循簡化版的 MVC 架構：

| 組件         | 負責內容                            |
|--------------|-------------------------------------|
| **Model**    | 使用 `SQLModel` 定義任務資料結構（`Task` 類別） |
| **Controller** | FastAPI 的路由處理函式，負責 CRUD 邏輯         |
| **View**     | Vue 前端 |

---

##  功能介紹

| 方法  | 路由               | 功能說明         |
|-------|--------------------|------------------|
| GET   | `/tasks`           | 取得所有任務     |
| GET   | `/tasks/{task_id}` | 取得指定任務     |
| POST  | `/task`            | 建立新任務       |
| PUT   | `/tasks/{task_id}` | 更新任務內容     |
| DELETE| `/tasks/{task_id}` | 刪除任務         |

每筆任務（Task）包含以下欄位：

- `id`: 自動產生的主鍵
- `title`: 任務標題
- `description`: 任務描述（可選）
- `done`: 是否完成（布林值）

---
