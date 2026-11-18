import json
from datetime import datetime, timezone, timedelta

def main():
    tz_tw = timezone(timedelta(hours=8))
    now_str = datetime.now(tz_tw).strftime("%Y-%m-%d %H:%M:%S")

    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # 嚴格遵守選罷法第 53 條封關規範：鎖定 11/17 前基準與 OLS 權重，僅更新同步時間與公開環境指標
    data["updated_at"] = now_str
    data["legal_status"] = "法定民調封關期間（鎖定 2026/11/17 前公開基準與中選會歷屆 OLS 權重）"

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"[{now_str}] Daily static data.json updated successfully.")

if __name__ == "__main__":
    main()
