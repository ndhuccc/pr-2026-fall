---
name: view-from-text
description: Turn a lecture note (lectures/lecNN.md) or pasted text into a complete JianBauDau slide deck saved as slides/lecNN.jbd.json in this course repo. Use when the user asks for 投影片, slides, JianBauDau, 把講義做成投影片, or lecNN.jbd.json.
---

# view-from-text(課程版)

把講義轉成 JianBauDau 完整簡報檔 `slides/lecNN.jbd.json`(格式 PresentationDocumentV3,與編輯器的 **Export** 相同)。老師用 JianBauDau 編輯器或播放器 **Open** 這個檔案。

**這個技能只產生草稿。** 排版是否好看、動畫順序是否合理,無法由程式判斷,必須由老師在 JianBauDau 中逐頁檢查。

技能位置:`.agents/skills/view-from-text/`。同資料夾的參考文件:

| 檔案 | 用途 |
|---|---|
| `AI_AGENT_FILE_FORMAT_SPEC.md` | 檔案格式、欄位、驗證規則(第「驗證規則與常見錯誤」一節必須逐條核對) |
| `PRESENTATION_DESIGN_GUIDE.md` | 版面原則:一個 Frame = 一個知識單元、配色對比、非矩形形狀不放文字 |
| `VISUAL_AND_LAYOUT_GUIDE.md` | 拆頁標準、色彩語意、版型、示意圖做法。設計每一頁前必讀 |
| `jbd_figure.py` | 選用。用 matplotlib 畫精準示意圖,包成 image 節點(需 `pip install -r requirements-lecture.txt`) |

> 規格檔提到的 `examples/photosynthesis-knowledge-units.json` 不在本資料夾。以規格內的「最小可行範例」為準。

## 1. 開始前

1. 讀 `AGENTS.md` §5.11 與 `slides/FORMATS.md`。
2. 讀 `lectures/lecNN.md`(NN 為週次)。講義是內容來源;投影片只呈現講義已有的內容,不要自行加入新觀點。
3. 讀完三份參考文件。
4. 若老師沒說明,預設 16:9,並依講義章節拆成知識單元。只有在無法判斷週次或內容範圍時才問老師。

## 2. 隱私與公開(硬規則)

課程網站是公開的,`slides/` 內的檔案會被提供下載,包含講者備註。

- **不要**寫入學號、成績、名單、電子郵件、Token、密碼。
- **不要**放解答(`labs/*/solution/`)或尚未考過的考題。
- **預設不寫** `speakerNotes`。只有老師要求時才加,並在回報中說明備註會公開。
- 圖片與影片用 `https://` 網址,或 `jbd_figure.py` 產生的內嵌 SVG。不要使用 `asset:` 參照。

## 3. 拆頁與設計

- 依 `VISUAL_AND_LAYOUT_GUIDE.md` §1 拆頁:每頁只回答一個問題,標題寫成結論。
- 每個講義章節或小節對應一個 Frame 節點與一個子 Scene(規格「Scene」一節的雙向對應規則)。
- 數學式用 `$...$`(行內)或單獨一行的 `$$`(區塊)。
- 配色取自規格與版型指南的色彩語意。Connector 的 `textColor` 必須用深色。
- 版面座標用本地座標,16:9 為 1280×720。

## 4. 產生檔案

- 用 Python 腳本在暫存目錄(不要放進 repo)組出 dict,再 `json.dump(..., ensure_ascii=False, indent=2)` 寫到 `slides/lecNN.jbd.json`。不要手打長 JSON。
- 所有 id 加上週次前綴(例如 `lec02-...`),避免撞名。
- `metadata`:`title` 寫課程與週次,`createdAt`/`updatedAt` 用當下 ISO 時間,`aspectRatio` 明確填 `"16:9"`。
- 圖片大小需控制在 20 MB 以內(超過會被 WARN)。

## 5. 驗證(必做)

1. 依規格「驗證規則與常見錯誤」第 1–15 條逐條自我檢查。驗證器沒有涵蓋的項目特別注意:
   - Connector 的 `sourceNodeId`/`targetNodeId` 必須同場景、不能是自己;`sourceHook`/`targetHook` 為 0–15 整數。
   - 每個節點的 `transform` 與 `width`/`height` 必須是有限數字,`width`/`height` > 0。
2. 執行:
   ```bash
   py scripts/check_slides.py slides/lecNN.jbd.json
   ```
   - **FAIL** 必須修正後重跑,直到沒有 FAIL。
   - **WARN** 逐項列給老師確認(講者備註、電子郵件、疑似學號、檔案大小、`aspectRatio`)。

## 6. 交付給老師

1. 說明檔案位置 `slides/lecNN.jbd.json`,以及檢查結果(FAIL 數、WARN 內容)。
2. 請老師在 JianBauDau 編輯器或播放器 **Open** 此檔,逐頁檢查排版、文字是否被截斷、步驟順序是否正確。
3. 若要在講義中連結投影片,依 `AGENTS.md` §5.11 更新 `lectures/lecNN.md` 或 `schedule.md`。
4. 依 `AGENTS.md` 的流程提交並推送。

## 不做的事

- 不產生「Import Scene」用的單頁或多頁 page spec。那是 JianBauDau App 內貼上匯入的流程,不是課程的交付格式。
- 不宣稱排版已驗證。只有 `check_slides.py` 的結構檢查與老師的目視檢查算數。
