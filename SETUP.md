# 教師設定指南(SETUP)

> 本文件給**教師**使用,說明如何把這份範本變成每學期的課程 Repo。
> 標示 🖱️ 的步驟必須在 GitHub 網頁端以你的帳號手動操作。

> 🤖 **想讓 AI Agent 帶著做?** 本文件的流程已寫成給 AI 的操作手冊 `AGENTS.md`;對 GitHub 不熟的老師請看 `START_HERE.md`。

## 一、一次性設定(只需做一次)

1. 🖱️ 在 GitHub 建立 Repo(例如 `course-template`),把本資料夾內容推上去:

   ```bash
   cd course-template
   git init -b main
   git add .
   git commit -m "init: 課程 Repo 範本"
   git remote add origin https://github.com/<你的帳號>/course-template.git
   git push -u origin main
   ```

2. 🖱️ *Settings → General → Template repository* 打勾,使其成為範本。
3. (建議)驗證範本本身健康:

   ```bash
   pip install -r requirements.txt
   LAB_TARGET=solution pytest labs -q   # 解答應全數通過
   pytest labs -q                        # starter 應全數失敗(表示測試有鑑別力)
   ```

## 二、每學期流程

### 步驟 1:由範本建立新 Repo
🖱️ 範本頁面按 **Use this template → Create a new repository**,命名如 `dl-2026-fall`。

### 步驟 2:填寫學期設定並套用

```bash
git clone https://github.com/<你的帳號>/dl-2026-fall.git && cd dl-2026-fall
cp semester.example.toml semester.toml     # 編輯 semester.toml
python scripts/new_semester.py --dry-run   # 預覽會改哪些檔案
python scripts/new_semester.py             # 正式套用(需要 Python 3.11+)
```

腳本會替換所有 `{{佔位符}}`(課名、學期、聯絡方式、`W01`~`W18` 週次日期等),
並列出**尚未填入**的佔位符,讓你補齊。

> 📌 **`deploy-site` 在範本 Repo 不會執行**(範本的 `mkdocs.yml` 還是佔位符,建置會失敗)。
> 要測試網站發佈,請在**套用過 `new_semester.py` 的學期 Repo** 操作:
> 該 Repo → *Actions* → 左側選 **deploy-site** → 右側 **Run workflow** → 選 `main` → 綠色 *Run workflow*。
> 需先完成下方的 Pages 設定(Source: GitHub Actions)。
> 私有 Repo 使用 Pages 需要 GitHub Pro / Team 等付費方案;免費帳號請改用公開 Repo(此時請勿放 `solution/`)。

### 步驟 3:啟用 GitHub 功能(🖱️ 網頁端)

| 功能 | 位置 | 說明 |
|---|---|---|
| Pages | Settings → Pages → Source 選 **GitHub Actions** | 課程網站;網址即 `SITE_URL` |
| Discussions | Settings → General → Features | 開放討論區(**新 Repo 預設關閉,不會從範本繼承,每學期都要重新勾選**) |
| Issues | 預設已啟用 | 已提供提問/勘誤/申請範本 |
| Projects | Projects → New project | 教學進度與專題里程碑看板 |
| Codespaces | 預設可用 | 已含 `.devcontainer/` |

### 步驟 4:作業自動批改(GitHub Classroom,🖱️)

1. 前往 <https://classroom.github.com> 建立 Classroom(綁定你的組織)。
2. 新增作業 → 選「使用本 Repo 作為 Template」。
3. 把邀請連結貼到作業說明(`assignments/hwNN/README.md`)。
4. 學生接受作業後會得到私人 Repo,推送即觸發 `autograde.yml`。

> ⚠️ 提供給學生的 Template **不應含有 `solution/`**。請在建立作業用的 Template 前,先刪除或移出 `labs/*/solution/`(見下節)。

### 步驟 5:設定解答釋出日

編輯 `release_schedule.toml`,為每個實驗填入日期。`deploy-site.yml` 每天自動重建網站,
日期一到,`labs/<lab>/solution.md` 就會出現在網站上,**不需手動操作**。

## 三、解答保密(重要)

`release_schedule.toml` 只控制**網站**。只要 `solution/` 與公開 Repo 一起被推送,
任何人都能在 Repo 內看到它。依你的需求擇一:

| 做法 | 適用 | 作法 |
|---|---|---|
| **A. 教師私有 Repo(推薦)** | 一般情況 | 維護一個私有 Repo 含完整內容(含 solution);只把「去除 solution」的版本公開或發給學生 |
| B. Repo 全程私有 | 修課人數少、Repo 只給修課學生 | 將學生加為 Collaborator(唯讀);網站另行發佈(私有 Repo 的 Pages 需付費方案) |
| C. 公開 Repo + 不放解答 | 不需自動釋出解答 | 解答另存他處,於截止後手動貼到網站 |

## 四、日常維運

| 想做的事 | 做法 |
|---|---|
| 新增講義 | 在 `lectures/` 新增 `lecNN.md`,推送後網站自動更新 |
| 新增實驗 | `cp -r labs/lab01 labs/lab02`,修改後在 `release_schedule.toml` 加日期 |
| 公告異動 | 編輯 `CHANGELOG.md`,並視需要發 Discussions 公告 |
| 學期結束封存 | 🖱️ Releases → 建立 `v{{學期}}` Tag;Settings → 勾選 Archive this repository |

## 五、佔位符一覽

| 佔位符 | 來源 |
|---|---|
| `COURSE_NAME` `COURSE_CODE` `SEMESTER` `UNIVERSITY` `DEPARTMENT` `INSTRUCTOR` `EMAIL` `GITHUB_USER` `REPO_NAME` `START_DATE` | `semester.toml` 必填 |
| `COURSE_DESCRIPTION` `CREDITS` `CLASS_TIME_LOCATION` `TA` `OFFICE_HOUR` `TEXTBOOK` `AI_POLICY` `TEAM_SIZE` | `semester.toml` 選填 |
| `REPO_URL` `SITE_URL` `YEAR` `W01`–`W18` | 自動推導 |
| 其他(如 `HW01_DUE`) | `semester.toml` 的 `[extra]` 區段 |

## 六、隱私與合規提醒

- **成績、學號、學生個資絕不放入公開 Repo**;`.gitignore` 已排除 `grades/` 與 `private/`。
- 使用學生程式碼相似度比對工具前,請先在課綱中告知學生。
- 公開考古題前,確認不會與本學期考題重複。
