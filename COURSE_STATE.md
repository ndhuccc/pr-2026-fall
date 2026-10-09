# 課程進度與決策紀錄(COURSE_STATE)

> **給 AI agent**:每次工作開始先讀本檔,結束前更新本檔。
> 勾選 `[x]` 表示完成;不要刪除舊紀錄,新紀錄加在「決策與異動紀錄」最上方。
> 此檔會被提交到 Git,**請勿寫入成績、學號、個資、密碼或 Token**。

## 基本資料

| 項目 | 內容 |
|---|---|
| 課程 | 圖型識別(AIIA50260) |
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
- [x] Step 6 提交並推送(commit 945b993)
- [x] Step 7a 啟用 Pages(Source: GitHub Actions),網址 https://ndhuccc.github.io/pr-2026-fall/
- [x] Step 7b 開啟 Discussions
- [x] Step 7c 手動觸發 `deploy-site` 並確認網站可開(run 37861833169 成功,網站回應 200)
- [ ] Step 8 初始化內容(週次主題、保留的 Lab/作業、解答釋出日、課綱)
- [ ] Step 9 向老師總結

## 待辦事項

(目前沒有)

## 決策與異動紀錄

(最新的在最上面。格式:`YYYY-MM-DD — 決定或異動內容`)

- 2026-10-09 — 老師決定:TA、Office Hour、AI 使用政策、HW01 發佈與截止日、分組人數、作業繳交規範先留空(相關檔案的佔位符已清空)。lectures/lec01.md 依第 1 週主題「課程介紹與圖形識別概論」改寫,舊內容(線性模型與梯度下降)已移除。
- 2026-10-09 — 依教學計畫表(115/1,科目代碼 AIIA50260)更新課程內容:課號改為 AIIA50260;學分 3 學分/3 小時;教科書與課程描述;評分改為平時 20% / 期中 25% / 期末 35% / 作業 20%(取代範本的實驗與專題比例);schedule.md 改為 17 週官方進度(期中 11/02、期末 12/28)。
- 2026-10-09 — 老師決定:第 4 週(9/28)與第 8 週(10/26)放假,採「壓縮合併單元」。期中前 8 個單元壓縮為 6 次課:Bayes(1)+(2) 合併、Linear(1)+(2) 合併;期中後 7 個單元不變;期中 11/02、期末 12/28 不變。學校期末評量 12/28–31,之後為寒假,無額外週次。
- 2026-10-09 — 移除範例實驗 labs/lab01–03(老師決定本學期尚無實驗,之後陸續加入;舊內容保留在 git commit 945b993)。autograde 的兩個 pytest 步驟改為無測試檔時略過;release_schedule.toml 清空 [solutions];README 與 lec01 移除實驗連結。
- 2026-10-09 — 啟用 Pages(workflow 來源)與 Discussions;手動觸發 deploy-site 成功,網站可開。
- 2026-10-09 — 建立 ndhuccc/pr-2026-fall(Private,由 course-template 產生);套用學期設定。第 1 週起始 2026-09-07(依 sys.ndhu.edu.tw 行事曆「全校開始上課」)。
- 2026-10-09 — 行事曆標示週一放假:第 4 週 9/28(孔子誕辰／教師節)、第 8 週 10/26(光復節補假),排程時需跳過。
- 2026-10-09 — 上課時間記為週一 14:10–17:00;上課地點未填(待補)。
- 未填選填欄位(老師決定先留空):AI_POLICY、OFFICE_HOUR、TA、TEAM_SIZE、HW01_DUE、HW01_RELEASE。
- 待辦:(1) Step 8 實驗加入時依 AGENTS §5.2 建立;若要以舊範例為起點,可用 `git checkout 945b993 -- labs/lab01` 還原。(2) 待老師提供後再補:TA、Office Hour、AI 使用政策、HW01 發佈與截止日、分組人數、作業繳交規範。(3) projects/README.md 的里程碑與 assignments/hw01 的題目仍是範本內容,需依本課程調整。
