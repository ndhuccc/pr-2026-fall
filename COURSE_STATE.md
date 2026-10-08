# 課程進度與決策紀錄(COURSE_STATE)

> **給 AI agent**:每次工作開始先讀本檔,結束前更新本檔。
> 勾選 `[x]` 表示完成;不要刪除舊紀錄,新紀錄加在「決策與異動紀錄」最上方。
> 此檔會被提交到 Git,**請勿寫入成績、學號、個資、密碼或 Token**。

## 基本資料

| 項目 | 內容 |
|---|---|
| 課程 | 圖型識別(CSIE6001) |
| 學期 | 2026 秋季(第 1 週起始 2026-09-07) |
| Repo | ndhuccc/pr-2026-fall |
| Repo 可見度 | Private |
| 使用的 agent 工具 | Claude(本次對話) |
| agent 能力等級 | L2(gh 已登入,可直接操作 Repo) |

## 建立學期的檢查表(AGENTS.md §3)

- [x] Step 1 老師有 GitHub 帳號
- [x] Step 2 用範本建立學期 Repo(2-A 自動完成:ndhuccc/pr-2026-fall)
- [x] Step 3 agent 取得 Repo 存取(gh clone)
- [x] Step 4 完成訪談,產生 `semester.toml`
- [x] Step 5 套用設定;網站建置與實驗測試驗證通過(starter 27 失敗、solution 27 通過)
- [ ] Step 6 提交並推送
- [ ] Step 7a 啟用 Pages(Source: GitHub Actions)
- [ ] Step 7b 開啟 Discussions
- [ ] Step 7c 手動觸發 `deploy-site` 並確認網站可開
- [ ] Step 8 初始化內容(週次主題、保留的 Lab/作業、解答釋出日、課綱)
- [ ] Step 9 向老師總結

## 待辦事項

(目前沒有)

## 決策與異動紀錄

(最新的在最上面。格式:`YYYY-MM-DD — 決定或異動內容`)

- 2026-10-09 — 建立 ndhuccc/pr-2026-fall(Private,由 course-template 產生);套用學期設定。第 1 週起始 2026-09-07(依 sys.ndhu.edu.tw 行事曆「全校開始上課」)。
- 2026-10-09 — 行事曆標示週一放假:第 4 週 9/28(孔子誕辰／教師節)、第 8 週 10/26(光復節補假),排程時需跳過。
- 2026-10-09 — 上課時間記為週一 14:10–17:00;上課地點未填(待補)。
- 未填選填欄位:AI_POLICY、COURSE_DESCRIPTION、CREDITS、HW01_DUE、HW01_RELEASE、OFFICE_HOUR、TA、TEAM_SIZE、TEXTBOOK。
- 待辦:Step 7 啟用 Pages/Discussions;Step 8 填 release_schedule.toml 解答釋出日(目前為佔位值 2099);補上課地點等選填欄位。
