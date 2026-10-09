---
name: view-from-text
description: Turn a lecture note (lectures/lecNN.md) or pasted text into a complete JianBauDau slide deck saved as slides/lecNN.jbd.json in this course repo. Use when the user asks for 投影片, slides, JianBauDau, 把講義做成投影片, or lecNN.jbd.json.
---

# view-from-text(課程版)

把講義轉成 JianBauDau 完整簡報檔 `slides/lecNN.jbd.json`(格式 PresentationDocumentV3,與編輯器的 **Export** 相同)。老師用 JianBauDau 編輯器或播放器 **Open** 這個檔案。

**這個技能只產生草稿。** 排版是否好看、動畫順序是否合理,無法由程式判斷,必須由老師在 JianBauDau 中逐頁檢查。

技能位置:`.agents/skills/view-from-text/`(路徑以 Repo 根目錄為基準)。

## 技能檔案

| 檔案 | 用途 | 何時讀 |
|---|---|---|
| `SKILL.md` | 本文件:流程、硬規則、交付 | 每次 |
| `AUDIT_CHECKLIST.md` | **所有稽核項目**,逐項勾選(A–J) | 交付前必讀並逐項核對 |
| `AI_AGENT_FILE_FORMAT_SPEC.md` | 格式、欄位、型別、驗證規則、Step、reveal、Connector、Markdown/LaTeX 語法 | 產生 JSON 前 |
| `PRESENTATION_DESIGN_GUIDE.md` | 巢狀 Scene/Frame 結構、Step 路徑、構圖(瞄準框)、視覺多樣性 | 設計結構前 |
| `VISUAL_AND_LAYOUT_GUIDE.md` | 拆頁、內容預算、色彩語意、版型 A–T、示意圖做法與嵌入預算 | 設計每一頁前 |
| `jbd_figure.py` | 用 matplotlib 畫精準 SVG 示意圖並包成 image 節點 | 需要幾何、函數、統計圖時 |
| `example-page-spec.json` | 單頁匯入範例(僅附錄 A 使用) | 附錄 A |

> 規格檔提到的 `examples/photosynthesis-knowledge-units.json` 與 `examples/` 資料夾不在本技能中。以規格內的「最小可行範例」為準。

## 1. 開始前

1. 讀 `AGENTS.md` §5.11 與 `slides/FORMATS.md`。
2. 讀 `lectures/lecNN.md`(NN 為週次)。講義是內容來源;投影片只呈現講義已有的內容,不加入新觀點。
3. 讀 `AI_AGENT_FILE_FORMAT_SPEC.md`、`PRESENTATION_DESIGN_GUIDE.md`、`VISUAL_AND_LAYOUT_GUIDE.md` 與 `AUDIT_CHECKLIST.md`。
4. 確認比例。預設 16:9;若要 4:3,頁面參考尺寸改為 960×720。只有在無法判斷週次或內容範圍時才問老師。

## 2. 隱私與公開(硬規則)

課程網站是公開的,`slides/` 內的檔案會被提供下載,包含講者備註。

- **不要**寫入學號、成績、名單、電子郵件、Token、密碼。
- **不要**放解答(`labs/*/solution/`)或尚未考過的考題。
- **預設不寫** `speakerNotes`。只有老師要求時才加,並在回報中說明備註會公開。
- 圖片用 `https://` 網址,或 `jbd_figure.py` 產生的內嵌 SVG。不使用 `asset:` 參照。

## 3. 內容來源規則(版面 §1.6)

- 保留原作者的比喻、口訣、數值例與習題,不另造。
- **不改數字。** 若講義中的公式因複製而損壞,先還原,再重新演算每個數值。
- 習題預設不附答案,除非講義有或老師要求。
- 警告與易錯點單獨成頁或單獨成卡。

## 4. 拆頁與設計

- **拆頁**:每頁只回答一個問題,標題寫成結論。拆頁觸發條件與內容預算見 `VISUAL_AND_LAYOUT_GUIDE.md` §1,數字與逐項檢查見 `AUDIT_CHECKLIST.md` D 節。
- **知識單元**:每個單元是一個 Frame,指向一個子 Scene。單元內可再巢狀,但不超過 3 層。跨單元的關係留在共同上層,用 Connector 表示(`PRESENTATION_DESIGN_GUIDE.md`)。
- **版型**:每頁先選一個主版型(A–T,`VISUAL_AND_LAYOUT_GUIDE.md` §3.1),依 §3.3 決策表選擇。相鄰頁不用同一版型,避免單調(§3.4)。
- **配色**:依 `VISUAL_AND_LAYOUT_GUIDE.md` §2 的色彩語意。一概念一色;Connector 標籤文字用深色。
- **示意圖**:能由位置、角度、形狀承載資訊的圖用 `jbd_figure.py` 產生(§4.1、§4.3–4.6);只是排版的概念草圖用原生節點。
- **構圖**:Step 的鏡頭要讓內容貼齊 16:9 瞄準框,不留大片空白(`PRESENTATION_DESIGN_GUIDE.md` 構圖建議)。
- **座標**:本地座標,16:9 為 1280×720,4:3 為 960×720。節點可略超出範圍,但不要大幅超出。

### 節點必填欄位

每個節點都必須有:`id`、`type`、`name`、`sceneId`、`transform`(`x`、`y`、`scaleX`、`scaleY`、`rotation`)、`width`、`height`、`zIndex`、`locked`、`style`、`text`。其他欄位依型別需要(例如 `shape` 需要 `shapeKind`,`frame` 需要 `frame`,`connector` 需要 `connector`,`image` 需要 `image`)。型別細節見規格「各種節點型別要另外填的內容欄位」。

node id 必須全域唯一。建議每份簡報使用週次前綴(例如 `lec02-…`)。

## 5. 產生檔案(完整簡報)

- 用 Python 腳本在暫存目錄(不要放進 repo)組出 dict,再以 `json.dump(..., ensure_ascii=False, indent=2)` 寫到 `slides/lecNN.jbd.json`。不要手打長 JSON。
- `metadata`:`title` 寫課程與週次,`createdAt`、`updatedAt` 用當下 ISO 時間,`aspectRatio` 明確填 `"16:9"` 或 `"4:3"`。
- 每個知識單元至少 2–3 個 Step:`enter-frame` 進場,接著 `scene-overview`、`focus-node` 或 `scene-point` 展開細節(需要時搭配 `reveal` 與 `initiallyHidden`),視需要退回上一層。所有 Step 串成一個扁平陣列,`order` 依序遞增 0、1、2…。
- Step 的 `label` 是「序號 + 結論短句」,≤ 20 字。
- 圖片大小控制在 20 MB 以內(超過會被 WARN)。

## 6. 稽核與驗證(必做)

1. **逐項核對 `AUDIT_CHECKLIST.md`**(A–J)。A 節是硬規則,違反會被 App 拒絕;其餘是設計品質。每項都要實際檢查,不是憑感覺。
2. 執行結構驗證:

   ```bash
   py scripts/check_slides.py slides/lecNN.jbd.json
   ```

   - **FAIL**:必須修正後重跑,直到沒有 FAIL。
   - **WARN**:逐項列給老師確認(講者備註、電子郵件、疑似學號、檔案大小、`aspectRatio`)。

`check_slides.py` 只檢查 A 節的一部分。Connector 的參照與掛點、變換數值、版型與色彩都必須由 `AUDIT_CHECKLIST.md` 人工核對。

## 7. 交付給老師

1. 說明檔案位置 `slides/lecNN.jbd.json`、`check_slides.py` 的結果(FAIL 數、WARN 內容),以及 `AUDIT_CHECKLIST.md` 中有哪些項目無法自動確認。
2. 請老師在 JianBauDau 編輯器或播放器 **Open** 此檔,並確認 `AUDIT_CHECKLIST.md` I 節的四項:
   - SVG 圖正常顯示、縮放清晰。
   - Export PDF 時 SVG 正常。
   - 播放器中正常播放。
   - 逐頁檢查排版、文字截斷與 Step 順序。
3. 若要在講義中連結投影片,依 `AGENTS.md` §5.11 更新 `lectures/lecNN.md` 或 `schedule.md`。
4. 依 `AGENTS.md` 的流程提交並推送。

## 8. 常見狀況處理

- **一次轉整週或整章**:依版面 §1 規劃頁數與版型序列(相鄰頁不重複版型),整批寫進同一份完整簡報,順序由 Step 陣列決定。
- **內容一頁裝不下**:依 §1.4 拆成多頁,或改用巢狀 Frame 結構(設計準則),不要擠進單一頁。
- **驗證失敗或圖片太大**:依錯誤訊息修正後重跑,不要略過。圖片超過預算時簡化圖、用 `rasterized=True`,或輸出 PNG(版面 §4.6)。
- **無法確定某個版型或色彩**:依版面 §3.3 與 §2 選擇,不要自行發明。

## 不做的事

- **不產生**「Import Scene」用的 page spec 作為課程交付檔。`check_slides.py` 會把 page spec(含 `pages` 的檔案)判為 FAIL,因此不得放進 `slides/`。只有老師明確要求把單頁貼進既有簡報時,才依附錄 A 產生,且不放進 `slides/`。
- 不宣稱排版已驗證。只有 `check_slides.py` 與老師的目視檢查算數。

---

## 附錄 A:單頁或多頁匯入(Import Scene)

只有老師明確要求「把這一頁貼進既有簡報」時才使用。輸出是 JSON 文字,老師自己貼進 App,不寫入 `slides/`。

### 單頁格式

```jsonc
{
  "label": "這一頁在時間軸卡片上顯示的名稱",
  // origin 可省略:省略時 App 會排在目標 Scene 既有頁面的最右邊。
  "origin": { "x": 0, "y": 0 },
  // insertAfterStepId 可省略:省略時接在目標 Scene 目前最後一個 step 後面。
  "insertAfterStepId": "step-id-可省略",
  "nodes": [ /* 完整 SceneNode 陣列,transform.x/y 用本地座標 */ ]
}
```

- `sceneId` 填任意字串即可,App 匯入時會覆寫。
- 通常**不要**給 `origin`,讓 App 自動排列。只有使用者明確指定位置時才給。
- 參考範例:`example-page-spec.json`。

### 多頁格式

```jsonc
{
  "pages": [
    { "label": "1 …", "nodes": [ /* 第 1 頁 */ ] },
    { "label": "2 …", "nodes": [ /* 第 2 頁 */ ] }
  ]
}
```

- 頁面依陣列順序匯入,每頁排在前一頁右邊,時間軸依序接在後面。通常不給 `origin`。
- 全部成功才會匯入。任何一頁出錯就整批不匯入,錯誤訊息會指出 `pages[幾]`。匯入後一次 Undo 可整批還原。
- 每頁的 node id 前綴要不同,整批之間以及與既有 id 都不能重複。
- 只有一頁時,用單頁格式即可。

### 給老師的操作步驟

1. 在 JianBauDau App 切到**場景圖模式(Scene mode)**。若目前在 Viewport mode,按頂端的「Scene」按鈕。
2. 在畫布空白處或任一既有 reticle 上**右鍵**,選 **「Import Scene」**。
3. 把 JSON 貼進對話框,按「Import」。
4. 匯入成功後,新頁面會以白色 reticle 出現在目前的 Scene,時間軸多一張卡片,接在最後一個 step 後面。請老師在時間軸中把卡片拖到正確順序。
5. 若匯入失敗(JSON 錯、id 撞名、驗證失敗),把錯誤訊息拿回來,依訊息修正後重新產生,不要略過。

仍需依 `AUDIT_CHECKLIST.md` 逐項核對。
