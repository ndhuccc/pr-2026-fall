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
- [x] Step 8 初始化內容(週次與放假處理、課綱與評分、第 1 週講義、解答釋出日不適用因無實驗)。HW01 與專題里程碑保留範本內容,待之後改寫。
- [x] Step 9 向老師總結(2026-10-09 完成)

## 待辦事項

(目前沒有)

## 決策與異動紀錄

(最新的在最上面。格式:`YYYY-MM-DD — 決定或異動內容`)

- 2026-10-09 — 老師採用講義技能的示意圖判準,並指定圖的三個主要功能:(1) 一目了然,以視覺取代較長的文字闡述;(2) 補強文字語意描述的精準度;(3) 把抽象的空間幾何描述轉化為具象的精準圖解。圖內不用中文標籤(所有工具皆同),中文說明放在圖說與正文。修改 `.agents/skills/textbook-lecture-notes/SKILL.md`:§3 的「視覺需求」與「圖的功能」改為必填;§4.6 的圖欄改為必填;§5 改為 §5.0 判準(三層:依知識點類型、讀者測試、去除無關圖;密度下限:每個非純定義知識點至少一張圖)與工具對照;§5.4 圖說加入讀圖指引與功能標記;§7 新增第 10–12 項(圖覆蓋率、圖內無中文、圖的功能檢查);§8 摘要改為圖覆蓋率與功能分布。`view-from-text` 的 §4A 尚未依此判準調整,待老師決定。
- 2026-10-09 — 依老師指示把課程網頁第 2 章 2.4 後半至 2.7 列為第 2 週的自主學習教材,並支援「每週多份講義與投影片」。來源:`https://ndhuccc.github.io/CCC-LNS/PR_115/Ch02-bayes-classifiers/index.html`(讀取日期 2026-10-09;該頁共 19 個知識點,KP01–KP06 已由 `lec02.md` 涵蓋)。新增 8 份講義、38 張圖:`lec02-linear-classifiers`(KP07–08)、`lec02-parameter-estimation`(KP09–10)、`lec02-bayesian-inference`(KP11–12)、`lec02-mixture-models-em`(KP13)、`lec02-nonparametric-density`(KP14–15)、`lec02-naive-bayes-and-nn`(KP16–17)、`lec02-bayesian-networks`(KP18)、`lec02-bayesian-network-inference`(KP19)。結構支援:`build_docs.py` 的下載頁改為每週可多份並標出代號;`doctor.py` 接受 `lecNN-<代號>` 命名;`lectures/README.md` 與 `slides/FORMATS.md` 新增命名規則;`schedule.md` 第 2 週列出必讀與選讀;`README.md` 導覽補充說明。驗證:網站建置成功;圖內無中文(38 支腳本掃描 0 處);中文超長句 0(英文僅剩純公式行);原創性最長相同中文字串 11–12 字(低於技能的 12 字上限);每份講義的圖說與 Caption 成對、圖片檔案都存在。三個需要老師確認的疑點:(1) `lec02-mixture-models-em` 的 EM 疊代表數字來自來源的 100 點資料,但來源未附該資料,子代理以同一實驗設計與固定種子重做並在文中註明,數字不會與網頁 demo 完全相同;(2) 來源的貝氏網路參數數量寫 13,實算為 14,已在講義標註;(3) 來源一處「1% 誤差時 3NN 約 1.03%」與其自身公式不符,子代理未採用並標註。
- 2026-10-09 — 老師指出 u08 預告圖(b)應畫成曲線,才看得出一次(線性)與二次(非線性)的區隔。原因:對角 Σ 會讓 x2 的二次項相消,邊界是平行直線,無法呈現彎曲;需要非對角項(相關)才會彎。改為 Σ2=[[4,0.5],[0.5,1]](對角 4 與 1 沿用 §5.3,相關 0.5 為示意值),邊界成為雙曲線,在水平軸交於 -2.67 與 1.22;左圖仍為單一直線 x1=1。同時修正填色方式(改用與白色預混的不透明淺色,避免 alpha 造成整片深色與左右顏色相反),並把說明文字移入面板內避免壓到標題。講義圖與投影片 u08 圖都已更新,圖說說明非對角項為示意值。驗證:腳本輸出與獨立重算一致(交點 -2.673、1.218,與 x2 無關的情形已改為彎曲);壓線檢查 0 處;目視確認;投影片 check_slides 與自製稽核 0 問題。`slides/lec02.jbd.json` 仍未提交,等老師檢查。
- 2026-10-09 — 以現行 view-from-text 規則(§4B/§4A)重製 lec02 投影片:頁距 1400→1440、每個 Frame 一個 step(zoom 1280/480)、每頁一個 scene-point(zoom 0.878、referenceViewport 1280×720、預留 100 單位標題列)、標籤去掉序號、根層不另加總覽 step。新增 4 張圖:u03 門檻取捨、u04 後驗與條件風險比較、u05 單調變換 √p 曲線、u08 共同共變異數(共用 Σ 一條直線 / Σ 不同兩條平行直線)。圖數 6→10,每頁至多一張。驗證:check_slides 通過;自製稽核 0 問題(結構、§4B 幾何、頁面邊界、壓線、字數預算、字級、每頁圖數、SVG 大小);u08 的數字獨立重算(-2.571、1.238 且與 x2 無關)。同時修正講義的正確性錯誤:先前誤述「邊界彎曲」,實為兩條平行直線(commit 8bf7793)。尚未提交 `slides/lec02.jbd.json`,等老師在 JianBauDau 檢查。
- 2026-10-09 — 老師選定 `lec02-gaussian-contours` 維持原值(Σ=I 對稱非對角 1.2 的示意矩陣),並要求 `lec02-shared-covariance` 改用講義數字(選項 C):μ1=(0,0)、μ2=(2,0),左圖兩類皆 Σ=I(邊界為直線 x1=1),右圖第二類 Σ=diag(4,1)(邊界彎曲,在水平軸交於 x1=-2.571 與 1.238,與 §5.3 相同)。圖說改為說明數字出自 §5.3,不再標示為示意。驗證:腳本輸出與獨立重算一致(左圖 g1-g2 在 x1=1 為 0;右圖二次方程根為 -2.571、1.238);壓線檢查 0 處;目視確認;圖說句子長度符合規範。
- 2026-10-09 — 以 lec02 試點新的講義示意圖判準(§5.0)。知識點 10 個,依類型判定必圖 10 張;既有 3 張(bayes-numbers、error-regions、qda-regions,腳本未改)之外新增 7 張:threshold-tradeoff(門檻取捨)、risk-flip(條件風險)、monotone-transform(單調變換)、gaussian-1d(高斯 μ 與 σ)、gaussian-contours(Σ 的等機率線)、discriminant-difference(g=g1-g2 的兩個零點)、shared-covariance(共同共變異數預告)。每張圖的圖說加入讀圖指引與〔功能〕標記,既有 3 張的圖說也補上。驗證:7 張新腳本執行成功;以獨立腳本(僅標準函式庫)重算講義與圖說中的全部數字,17 項全數吻合;圖內文字無中文(腳本掃描 + 目視);以自製檢查器檢查文字方塊與線條重疊,7 張新圖 0 處(修正前有 6 處壓線);7 張全部目視確認;可讀性:圖說無超過 40 中文字或 25 英文單字的句子;網站建置成功。gaussian-contours 與 shared-covariance 為示意圖,數值為舉例,已在圖說標明。§7 小結與 §8 練習為純條列與純數字例,依 §5.0 不需要圖。尚未提交,等老師看圖。
- 2026-10-09 — 老師決定保留已公開的 `slides/lec02.jbd.json`(commit `2a3108e` 等;deploy-site 於 15:23 部署成功,網站可下載)。注意:此檔在老師於 JianBauDau 中目視檢查之前已先提交並部署,違反 SKILL.md §7 的順序。尚待辦:(1) 老師在 JianBauDau 中逐頁檢查排版、截斷、Step 與 reticle 一對一、播放構圖;(2) 若檢查發現問題,修正後重新提交。u03 門檻變化圖仍未決定。`check_slides.py` 的修正已在 HEAD。
- 2026-10-09 — lec02 投影片補齊必圖:u05 第 2 頁加判別差 g(x) 與決策邊界圖(R6,數字沿用 u07 的一維例子,零點 x≈-2.571、1.238);u06 第 1 頁加一維高斯曲線(R1),第 3 頁加等機率橢圓(R2,示意)。版面:收窄對應頁的文字欄重排,並修正 u06 第 2 頁既有的標籤與公式框重疊 3 px。`FIGURE_RECIPES.md` 新增 R6(已實際執行)。`slides/lec02.jbd.json` 已重新產生:合併後 check_slides 通過;結構檢查 0 問題;每頁至多一張圖。仍未提交 deck 與 check_slides.py 的修正,等老師在 JianBauDau 檢查。尚未處理:u03 門檻變化圖(待決定)。技能同步至 ndhuccc/course-template。
- 2026-10-09 — 示意圖偏少的原因與修正。原因:(1) 盤點時以「既有 PNG 是否存在」決定畫圖,未依 VISUAL §4.1 的內容類型判斷;(2) 派工時我在 manifest 與子代理任務中把 u03、u04–u06、u08–u09 設為「無圖」,其中 u05(判別函數)與 u06(高斯曲線、等機率橢圓)屬必圖;(3) 技能指引把圖的判準寫成「能承載資訊的圖才用」,沒有規定哪些內容必須有圖,AUDIT G1 只問理由是否成立;(4) 稽核時只檢查圖的大小與 alt,未檢查圖覆蓋率。修正:新增 `FIGURE_RECIPES.md`(R1 一維高斯、R2 等機率橢圓、R3 判別函數與決策邊界、R4 誤判陰影、R5 統計圖;已實際執行,皆產生 SVG 並通過裁切檢查);SKILL.md 新增 §4A 圖型對照表(函數、分布、幾何、決策邊界、門檻與面積、統計圖為必圖)、盤點與派工須列圖需求、§1A 稽核加圖覆蓋率;AUDIT G1 改寫,新增 G16–G18 與 K12。尚未處理:lec02 草稿仍缺 u05、u06 的必圖(以及 u03 的門檻變化圖,待決定),未提交。
- 2026-10-09 — `view-from-text` 新增長文本流程(SKILL.md §1A,稽核 K 節):篇幅超過約 3,000 字或預估超過 6 個單元時,(1) 先列知識單元表與待決事項給老師,確認後才處理;(2) 每批 3–4 單元;(3) 有子代理時平行處理,同時最多 6 個,子代理只輸出 fragment 檔,不改根場景、不跑 check_slides;(4) 主代理逐批稽核 D–H 節與契約後才合併,合併為唯一整合負責人。驗證:用兩個暫存單元合併,`check_slides.py` 通過;故意錯配 parentFrameId 的 fragment 被擋下。門檻數字與批次大小為預設值,可依老師需求調整。
- 2026-10-09 — `.agents/skills/view-from-text/` 補齊可攜版的所有指引與稽核項目。新增 `AUDIT_CHECKLIST.md`(A 格式硬規則 1–15、B 不報錯但出錯、C 生成流程 1–8、D 拆頁與內容預算、E 色彩、F 版型與單調、G 示意圖與嵌入預算、H 簡報結構與構圖、I 老師需確認項目、J 課程專用規則)。SKILL.md 補上 4:3 尺寸、節點必填欄位、構圖與瞄準框、常見狀況處理,以及附錄 A「Import Scene」單頁/多頁格式與老師操作步驟(不進 `slides/`);新增 `example-page-spec.json`。驗證:可攜版 18 個勾選項與版面 §2.1 經機械比對;16 項逐字比對失敗係改寫用語所致,已逐項人工對照確認語意覆蓋。未納入:可攜版 README(描述可攜包本身)與規格引用但不存在的 `examples/`。
- 2026-10-09 — 新增課程版投影片技能 `.agents/skills/view-from-text/`(來源:`~/.claude/skills/view-from-text-portable`)。目的:從 `lectures/lecNN.md` 產生完整的 JianBauDau 簡報 `slides/lecNN.jbd.json`,由 `scripts/check_slides.py` 驗證。改動:保留規格與版面指南、`jbd_figure.py`;SKILL.md 改寫為課程流程(完整文件、隱私與公開規則、必做驗證、不做 Import Scene 單頁流程);AGENTS.md §5.11 加一行指向。驗證:暫存樣本(Frame/子場景/Connector/Step/reveal/SVG 示意圖)通過 `check_slides.py`(exit 0);故意破壞 Frame↔子場景對應被擋(exit 1)。注意:驗證器未涵蓋 Connector 掛點與 transform 數值,SKILL.md 要求人工核對;排版須由老師在 JianBauDau 中目視確認。規格引用的 `examples/` 範例檔不在可攜版中。更正:先前「`render_formula.py` 不存在」的判斷有誤,該檔位於 `.agents/skills/textbook-lecture-notes/scripts/`。
- 2026-10-09 — 依老師指示(選項 2)與 `ndhuccc/course-template` 同步播放器下載連結:`scripts/build_docs.py` 改為範本版本(`PLAYER_URL` 與下載頁區段),`slides/FORMATS.md` 補上「播放器下載」一節(以 LF 插入,範本為 CRLF,內容相同)。範本既有 commit `34f13ff` 已含相同功能,未覆寫範本。驗證:兩檔與範本內容一致(忽略 CR);`build_docs.py` 與 `mkdocs build` 成功;推送後 `deploy-site`(run 37873707204)成功;線上 `slides/` 頁面含連結(回應 200)。
- 2026-10-09 — 投影片下載頁(`slides/`)加入 JianBauDau 播放器(Windows, 1.0.0)下載連結,來源為 `ndhuccc/IDL115` 的 GitHub Release(`player-v1.0.0/JianBauDau-Player-1.0.0.exe`)。實作:`scripts/build_docs.py` 新增 `PLAYER_URL` 常數,由 `write_slides_index` 產生於下載頁。驗證:連結回應 200;`mkdocs build` 成功;推送後 `deploy-site`(run 37873286728)成功,線上 `slides/` 頁面已含連結。注意:連結指向他人專案的 Release,若 IDL115 刪除或改版,需更新 `PLAYER_URL`。
- 2026-10-09 — 配合 JianBauDau 投影片(JSON)調整 repo 設計:`slides/` 接受 `lecNN.jbd.json`、`lecNN.pptx`、`lecNN.pdf`、`lecNN.html`;新增 `scripts/check_slides.py`(JianBauDau 完整文件的結構與隱私檢查,範例檔通過、page spec 與壞檔被擋)、`slides/FORMATS.md`(老師用格式說明,不上網站)。`build_docs.py` 讓 slides/ 的 .json/.pptx 可下載,並自動產生網站下載頁;`doctor.py` 新增投影片檢查;AGENTS.md 新增 §5.11 與地圖列;README 更新列。發現:課程網站為公開網址,投影片與講者備註會公開。
- 2026-10-09 — 修正 `lec02-error-regions` 左圖:陰影用加權值 $0.5\,p(x\mid\omega)$ 計算,但圖上畫的是未加權密度,陰影上緣對不上曲線。改為畫加權密度 $P(\omega_i)p(x\mid\omega_i)$,陰影直接落在曲線之下,每塊面積 0.0793(合計 0.1587)。圖說與替代文字同步更新;講義技能 §7 第 9 項新增「陰影或面積圖」稽核。
- 2026-10-09 — 依課程網頁 Chapter 2(以貝氏決策理論為基礎的分類器)撰寫第 2 週講義 `lectures/lec02.md`。範圍為教科書 2.1–2.4 的前半(貝氏決策、誤判機率與風險、判別函數、高斯貝氏分類器/QDA);2.4 後半的 LDA 超平面與 2.5 以後(參數估計、MAP、EM、無母數、kNN、Naive Bayes、貝氏網路)留待後續週次。圖:`lec02-bayes-numbers`、`lec02-error-regions`、`lec02-qda-regions`(Matplotlib,數字已驗算,已目視檢查)。原創性檢查通過(唯一重複為章名引用)。
- 2026-10-09 — 修正 `lec01-design-loop`:圖上只剩一條回饋路徑,但圖說與正文寫「任何較早的階段」。原因:為避免虛線穿過方塊,刪除了回到「特徵生成」的細虛線,卻沒有重新對照圖說。已重畫兩條回饋路徑(粗虛線回特徵選擇、細虛線繞過上方回特徵生成),圖說同步更新。講義技能新增「圖說先行」、「排版衝突時改佈局、不刪元素」與第 7 節第 9 項「圖說與圖形一致性稽核」。稽核結果:圖說三項主張(四階段順序、兩條回饋路徑、細虛線不穿過方塊)皆與圖檔相符。
- 2026-10-09 — 圖片改用文字代碼編號(不用數字序號,增刪圖片時不必重新編號):`lec01-feature-plane`、`lec01-learning-settings`、`lec01-design-loop`,檔名、腳本與圖說使用同一代碼。每張圖加上中英圖說。講義技能 §5.4 已更新此規則。
- 2026-10-09 — 老師指示:之後課程 Repo 的變更直接 push 到 `main`,不需逐次確認。範本(`ndhuccc/course-template`)的變更仍需先確認。
- 2026-10-09 — 修正網站公式:課程網站的 MathJax 不支援 `\boldsymbol`,會顯示紅色的 `\boldsymbol` 文字。`lectures/lec01.md` 的 4 處改為 `\mathbf`;講義技能 §4.4 新增此規則。
- 2026-10-09 — 依課程網頁 Chapter 1(Introduction)用新版講義技能改寫 `lectures/lec01.md`(繁中英對照、高中可讀、補充素材標 [補充]/[Added])。新增 `assets/figures/lec01_fig1.py`(模擬特徵平面)、`lec01_fig2.py`(三種學習方式)、`lec01_fig3.py`(設計迴圈),已目視檢查。網頁中的教科書圖與 AI 生圖提示未直接使用。原創性檢查通過(剩餘重複為專有名詞與章名)。
- 2026-10-09 — `lectures/lec01.md` 改寫為繁體中文與英文對照,加入決策規則的數字例(已用 Python 驗算)與示意圖 `assets/figures/lec01_fig1.png`(Matplotlib 腳本 `assets/figures/src/lec01_fig1.py`,已目視檢查)與術語表。
- 2026-10-09 — 新增講義製作技能,放在 Repo 內 `.agents/skills/textbook-lecture-notes/`(教科書 PDF → 高中可讀的碩士講義)。新增 `scripts/render_formula.py`(KaTeX + Playwright 公式圖,已測試)與 `requirements-lecture.txt`;AGENTS.md §5.1 加入指引。
- 2026-10-09 — 老師決定:TA、Office Hour、AI 使用政策、HW01 發佈與截止日、分組人數、作業繳交規範先留空(相關檔案的佔位符已清空)。lectures/lec01.md 依第 1 週主題「課程介紹與圖形識別概論」改寫,舊內容(線性模型與梯度下降)已移除。
- 2026-10-09 — 依教學計畫表(115/1,科目代碼 AIIA50260)更新課程內容:課號改為 AIIA50260;學分 3 學分/3 小時;教科書與課程描述;評分改為平時 20% / 期中 25% / 期末 35% / 作業 20%(取代範本的實驗與專題比例);schedule.md 改為 17 週官方進度(期中 11/02、期末 12/28)。
- 2026-10-09 — 老師決定:第 4 週(9/28)與第 8 週(10/26)放假,採「壓縮合併單元」。期中前 8 個單元壓縮為 6 次課:Bayes(1)+(2) 合併、Linear(1)+(2) 合併;期中後 7 個單元不變;期中 11/02、期末 12/28 不變。學校期末評量 12/28–31,之後為寒假,無額外週次。
- 2026-10-09 — 移除範例實驗 labs/lab01–03(老師決定本學期尚無實驗,之後陸續加入;舊內容保留在 git commit 945b993)。autograde 的兩個 pytest 步驟改為無測試檔時略過;release_schedule.toml 清空 [solutions];README 與 lec01 移除實驗連結。
- 2026-10-09 — 啟用 Pages(workflow 來源)與 Discussions;手動觸發 deploy-site 成功,網站可開。
- 2026-10-09 — 建立 ndhuccc/pr-2026-fall(Private,由 course-template 產生);套用學期設定。第 1 週起始 2026-09-07(依 sys.ndhu.edu.tw 行事曆「全校開始上課」)。
- 2026-10-09 — 行事曆標示週一放假:第 4 週 9/28(孔子誕辰／教師節)、第 8 週 10/26(光復節補假),排程時需跳過。
- 2026-10-09 — 上課時間記為週一 14:10–17:00;上課地點未填(待補)。
- 未填選填欄位(老師決定先留空):AI_POLICY、OFFICE_HOUR、TA、TEAM_SIZE、HW01_DUE、HW01_RELEASE。
- 待辦:(1) 待老師提供後再補:TA、Office Hour、AI 使用政策、HW01 發佈與截止日、分組人數、作業繳交規範。(2) HW01 與期末專題里程碑為範本內容,保留中,待依課程改寫。(3) 之後每週:新增講義、公告異動、處理 Issue、補充欄位;實驗加入時依 AGENTS §5.2,舊範例可用 `git checkout 945b993 -- labs/lab01` 還原。
