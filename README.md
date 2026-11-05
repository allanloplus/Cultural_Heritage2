# Allan Lo 和你逛文化（第二網站）

導覽員 **Allan Lo** 與 AI 小助手 **阿拉蕾** 帶你逛臺灣各縣市的文化資產。

- 規劃設計：Allan Lo，https://www.123hi.org，2026年11月
- 使用 AI 工具：Claude Opus 5.5

這是網站的**第二個 repo**。GitHub Pages 每個網站上限 1 GB，全臺做完約 1.23 GB，所以縣市分放兩個網站：

| 網站 | repo | 網址 | 放什麼 |
|---|---|---|---|
| 第一網站 | [allanloplus/Cultural_Heritage](https://github.com/allanloplus/Cultural_Heritage) | https://cultural.123hi.org/（自訂網域；舊網址 allanloplus.github.io/Cultural_Heritage/ 會自動轉過去） | 全站首頁、共用程式（`assets/`）、所有工具（`tools/`）、作業手冊，以及嘉義市、嘉義縣、雲林縣、臺南市、高雄市、屏東縣、臺東縣、金門縣、宜蘭縣、花蓮縣、連江縣、澎湖縣、基隆市 |
| 第二網站（本 repo） | allanloplus/Cultural_Heritage2 | https://cultural2.123hi.org/（自訂網域；舊網址 allanloplus.github.io/Cultural_Heritage2/ 會自動轉過去） | 只放縣市資料夾：臺北市、新北市、桃園市、新竹市、新竹縣、苗栗縣、臺中市、彰化縣、南投縣（完成後陸續加入） |

目前開放：**南投縣**（https://cultural2.123hi.org/nantou-county/）、**彰化縣**（https://cultural2.123hi.org/changhua-county/）、**臺中市**（https://cultural2.123hi.org/taichung-city/）、**新竹市**（https://cultural2.123hi.org/hsinchu-city/）、**新竹縣**（https://cultural2.123hi.org/hsinchu-county/）、**桃園市**（https://cultural2.123hi.org/taoyuan-city/）、**苗栗縣**（https://cultural2.123hi.org/miaoli-county/）。

- 本 repo 根目錄的 `index.html` 會自動轉到第一網站的全站首頁 https://cultural.123hi.org/。
- 這裡的縣市頁用第一網站的網址 `https://cultural.123hi.org/assets/…` 載入共用程式與角色圖，`https://cultural.123hi.org/assets/js/cities.js` 提供切換縣市選單；「全站首頁」連回 `https://cultural.123hi.org/`。網址設定在第一網站 `assets/js/cities.js` 的 `SITES`。
- 兩個網站的網域不同，文資護照、造訪紀錄存在各自網站的瀏覽器儲存空間（每個縣市本來就各有一本護照）。
- 縣市資料夾由第一網站的工具產生（`tools/build_data.py`、`tools/gen_audio.py`、`tools/fetch_images.py` 與 `tools/newcity/`），請不要手動修改 `index.html`、`js/data.js`、`audio/cues.js`。

## 作業方式

完整流程、規則與兩個網站的分工，請看第一網站的 **[作業手冊 `tools/newcity/README.md`](https://github.com/allanloplus/Cultural_Heritage/blob/main/tools/newcity/README.md)**（〈兩個網站〉一節）。重點：

1. 新 session 要同時掛載 `allanloplus/Cultural_Heritage` 與 `allanloplus/Cultural_Heritage2`（推送權限），兩個 clone 放在同一層目錄（例如 `/home/user/Cultural_Heritage` 與 `/home/user/Cultural_Heritage2`），或用環境變數 `CH2_DIR` 指定第二個的位置。
2. 本機預覽：在第一網站執行 `python3 tools/serve.py 8766`，它會同時提供 `/Cultural_Heritage/` 與 `/Cultural_Heritage2/`，並把頁面裡第一網站的正式網址換成本機路徑。
3. 每個放在這裡的縣市要開兩個 PR：縣市資料夾的 PR 開在本 repo；`cities.js`、入口頁問候語與語音、README、容量紀錄的 PR 開在第一網站。**先合併本 repo，再合併第一網站。**

## 上線

Settings → Pages → Build and deployment → Source 選 **Deploy from a branch**，Branch 選 **`main`**、資料夾 **`/ (root)`**。

---

Copyright © 2026 Allan Lo. 文字內容與程式碼版權所有；第三方資料與照片依各自授權。
