圖型識別 第四章 KP01：XOR 與線性分類的限制 — 逐字稿審閱版

對象：大學三年級。語言：繁體中文。狀態：草稿，待教師審閱。

閱讀入口：kp01-transcript-review.pdf（GitHub可預覽，亦可下載）
網頁版：kp01-transcript-review.html（下載後以瀏覽器開啟）
逐頁純文字：script/lec05-kp01-p001.txt 至 p012.txt。
第9–12頁為延伸閱讀；來源簡報有12個內容頁，另排除1個根場景導覽停點。
lec05沿用課程第5週檔名前綴，內容仍為第四章。

本次僅保存逐字稿，未生成音檔，未接入播放器，未上線課程網站。
來源簡報草稿已另存於 materials/lec05-kp01-xor.jbd.json；manifest保留雜湊與真實stepId，12份TXT對應同一版本。

檢查：逐頁內容對照警告0，12份TXT與工作資料一致。教師尚未審閱，reviewed全部保留false。
下載：在GitHub開啟PDF後使用下載按鈕；純文字可用Raw檢視並儲存。

講義與簡報草稿（待教師驗收，未上線網站）

materials/lec05-kp01-xor-lecture.pdf：講義PDF，GitHub可預覽及下載。
materials/lec05-kp01-xor-reading.html：離線講義閱讀版。
materials/lec05-kp01-xor.html：離線簡報，12內容頁加1導覽步驟。
materials/lec05-kp01-xor.jbd.json：可編輯JianBauDau原檔。
materials/KP01-XOR-review.zip：完整下載包，含Markdown、圖檔、繪圖程式及原有目錄結構。
materials/preview-1.png、preview-2.png：近似預覽縮圖，不是JianBauDau原生畫面。

HTML請下載後以瀏覽器開啟。講義閱讀版與簡報HTML請放在同一資料夾，讓講義中的簡報連結正常運作。
正式教材尚未寫入lectures/、slides/或assets/，也未同步課程進度表；先存於此處，以免先行發布。
原生播放器與其PDF匯出仍待驗收。8頁主線工具估28分鐘，4頁延伸不計；原先暫配15分鐘的時間差異待整章配置調整。
本次沒有漫畫、音檔。逐字稿另見同目錄的審閱版與script/。

下一批KP02–KP05講義與簡報（草稿，待教師驗收）

每個KP在materials/提供同名的 -lecture.pdf、-reading.html、.html簡報、.jbd.json原檔及-review.zip完整來源包。
KP02：lec05-kp02-two-layer-perceptron（講義8頁；簡報9個內容頁）
KP03：lec05-kp03-polyhedral-codes（講義8頁；簡報10個內容頁）
KP04：lec05-kp04-three-layer-perceptron（講義8頁；簡報11個內容頁）
KP05：lec05-kp05-constructive-methods（講義12頁；簡報13個內容頁）

合計43個內容頁；每份HTML另有1個根Frame導覽步驟。
計畫與檢查說明：materials/KP02-KP05-plan.txt、KP02-KP05-report.txt。
本批沒有漫畫、逐字稿、音檔。未正式發布課程網站；下一批KP06–KP09尚未製作，其中KP08規劃為自主學習。

保留更正：兩層網路不只可形成凸區域；三層表示足夠不等於每次tiling都只長三層。
圖與算例均有來源或補充標示；純化例是解析教學構造，不宣稱pocket實驗或完整原演算法重現。
已完成公式驗算、43頁近似預覽及雙尺寸HTML檢查；原生JianBauDau播放與其PDF匯出仍待驗收。

KP03重做版（2026-10-24，草稿，待教師驗收）

依 view-from-text 新增的 C12–C18（術語先白話、標題講明白、疑問接力、空間內容必有圖）重做 KP03，取代前一版：
materials/lec05-kp03-polyhedral-codes.*：簡報（11頁：主線9頁＋延伸2頁）、離線簡報HTML、講義PDF、講義閱讀HTML、完整來源包（含繪圖程式、術語表、稽核與冷讀者紀錄）。
本版為每頁配代數與幾何對照圖（共11張，含立方體圖、缺口圖、中點圖等補充圖）；已通過 check_slides.py 與 audit_deck.py（FAIL 0）。
冷讀者檢查做兩輪（獨立子代理），評分仍為3/5，詳見來源包內 COLD_READER.md；原生JianBauDau播放與PDF匯出尚未驗收。
KP01、KP02、KP04、KP05仍為舊版，待依新規範重做。

KP03中文版與英文版（2026-10-24，分開製作，可分別下載；草稿，待教師驗收）

中文版：materials/lec05-kp03-polyhedral-codes-zh-download.zip（簡報HTML、簡報原檔、講義PDF、講義閱讀HTML、Markdown、圖檔）。
英文版：materials/lec05-kp03-polyhedral-codes-en-download.zip（內容相同，另寫英文，不是機器剪貼）。
同一批檔案也單獨放在 materials/：lec05-kp03-polyhedral-codes-zh.* 與 -en.*（.jbd.json、.html、-lecture.pdf、-reading.html）。
先前的中英對照版保留不動（lec05-kp03-polyhedral-codes.*）；教師決定採用哪一套後，再刪除不用的版本。
兩個單語簡報都通過 check_slides.py 與 audit_deck.py --monolingual（FAIL 0）；兩份講義通過 audit_lecture.py --lang（FAIL 0）。
英文版的簡報標題、術語卡、講者備註、圖的替代文字與講義全部另寫；來源包（-review.zip）含兩種語言的組裝程式與術語表。

KP01、KP02 中文版與英文版（2026-10-25，依新規範重做，分開製作、可分別下載；草稿，待教師驗收）

KP01（XOR 與一條線的極限）：materials/lec05-kp01-xor-zh-download.zip、-en-download.zip；同批檔案也單獨放在 materials/lec05-kp01-xor-zh.*、-en.*。
KP02（兩層感知器）：materials/lec05-kp02-two-layer-perceptron-zh-download.zip、-en-download.zip；同批檔案也單獨放在 materials/lec05-kp02-two-layer-perceptron-zh.*、-en.*。
各 11 頁（主線 8 頁＋延伸 3 頁），每頁配代數與幾何對照圖；簡報通過 audit_deck.py --monolingual（FAIL 0）、check_slides.py，講義通過 audit_lecture.py（FAIL 0）。
冷讀者檢查（獨立子代理）：KP01 兩輪 4/5；KP02 一輪 3.5/5，已修標題與空心點說明，第二輪尚未做。詳見各 -review.zip 內 COLD_READER.md。
舊的中英對照版保留不動，待教師決定後再刪。KP04、KP05 仍為舊版，下一批重做。原生 JianBauDau 播放與 PDF 匯出尚未驗收。

KP04、KP05 中文版與英文版（2026-10-25，依新規範重做，分開製作、可分別下載；草稿，待教師驗收）

KP04（三層感知器：逐碼偵測再合併）：materials/lec05-kp04-three-layer-perceptron-zh-download.zip、-en-download.zip；同批檔案也單獨放在 materials/lec05-kp04-three-layer-perceptron-zh.*、-en.*。
KP05（構造式方法：從訓練點長出網路）：materials/lec05-kp05-constructive-methods-zh-download.zip、-en-download.zip；同批檔案也單獨放在 materials/lec05-kp05-constructive-methods-zh.*、-en.*。
各 11 頁（主線 8 頁＋延伸 3 頁），每頁配代數與幾何對照圖；簡報通過 audit_deck.py --monolingual（FAIL 0）、check_slides.py，講義通過 audit_lecture.py（FAIL 0）。
冷讀者檢查（獨立子代理，模型模擬）：KP04 一輪 4/5、KP05 一輪 3.5/5，已修正主要缺失，第二輪尚未做；KP05 p8（最近鄰）已依教授指示移到延伸。詳見各 -review.zip 內 COLD_READER.md。
至此 KP01–KP05 都已依新規範重做；舊的中英對照版保留不動，待教師決定後再刪。原生 JianBauDau 播放與 PDF 匯出尚未驗收。

KP05 調整(2026-10-25):依教授指示,把原第 8 頁「最近鄰」移到延伸;主線 7 頁、延伸 4 頁,「先固定架構再學權重」的下一個 KP 問題改放主線最後一頁。簡報、講義與下載包已重新產生。

第二輪冷讀與修正(2026-10-25):KP02(3.5/5)、KP04(3.5/5)、KP05(4/5)各做第二輪冷讀,已修正圖例、標籤位置、編號與用語不一致(KP04 將「三塊 A 區」改為「三個編碼區」、p9 例子說明為「本做法每格一個偵測器」;KP05 補 z2 的幾何推導與 C 的條件說明;KP02 補圖例與箭頭)。簡報、講義與下載包已重新產生。

章節總覽頁與舊版清理(2026-10-25,依教授指示):
- 新增第四章路線圖(總覽,8 頁):materials/lec05-kp00-overview-zh-download.zip、-en-download.zip;同批檔案也單獨放在 materials/lec05-kp00-overview-zh.*、-en.*。每頁回顧一個知識點的問、答與留下的問題,最後一頁做整章回顧;簡報稽核 FAIL 0。
- 已刪除 KP01–KP05 舊的中英對照版簡報(materials/lec05-kpNN-<主題>.html 與 .jbd.json 共 10 個檔);舊版的講義 PDF、閱讀 HTML、review.zip 等其他檔案保留。注意:上方 KP01 逐字稿相關說明提到的 materials/lec05-kp01-xor.jbd.json 與 .html 已不存在,可從 git 歷史取回(例如 commit ceee760)。
- 教授已在 JianBauDau 驗證新版簡報的播放與 PDF 匯出。

依外部審查修正(2026-10-25):
- 內容正確性:KP04 把偵測器的分數 h 與階梯後的 0／1 位元 b 分開寫,第 6 頁輸出式改為 q=b000+b110+b111−0.5(原寫成分數相加,照字面代入會得到錯誤結果);KP01 中文第 5 頁的 g(M) 二分之一因跳脫字元遺失而消失,已修正。
- 版面:KP05 英文第 8 頁標題與銜接條重疊(52 單位)、總覽英文第 2 頁同樣問題,已縮短標題。
- 教學補強:KP01 第 7 頁標題與說明改為「不管怎麼訓練,一條線都無法把 XOR 全分對」並說明訓練不保證找到最佳線;KP02 第 1 頁加網路接線圖、「隱藏編碼」移到第 3 頁定義;KP03 第 9 頁在畫面寫明「固定這三條隱藏線時」;KP04 第 3 頁改為先算例子再歸納;KP05 第 3 頁明寫輔助線為示範用手動選定、第 6 頁分開「同層」與「跨層」兩種進展並註明條件、最近鄰的 a、b 改為 u、v。
- 技能與工具(.agents/skills/view-from-text):audit_deck.py 新增 B10(文字框互相重疊)、B11(控制字元)、J4(co_defined 術語須在卡上真的被定義)、講義圖辨識修正;新增 tools/check_arithmetic.py(重算頁面上所有純數字等式);preview_deck.py 在 KaTeX 未完成時重試並警告;AUDIT_CHECKLIST 新增 W 節(驗算頁面實際符號、最終版證據);KP03 術語表的 aliases 改為 co_defined。
- 尚未處理(最終版冷讀者提出、影響較小):KP02 第 2 頁 g1/g2 同時當單元與線名、KP03 第 10 頁題 2 解答直接印出、KP04 第 9 頁格子需數線才能確認、圖內英文標註。修改後的最終版尚未再做一輪冷讀。
