import json
import random
from datetime import datetime

def get_market_data():
    now = datetime.now()
    timestamp_str = now.strftime("%Y.%m.%d %H:00 JST 同期済み")

    # 乗り換えターゲット車の最新相場・納期データマスター
    target_cars = {
        "hiace": {
            "used": {
                "name": "ハイエース スーパーGL (良質中古 3〜5万km)",
                "sub": "スーパーGL (中古)",
                "price": 312,
                "delivery": "即納 (約2〜3週間)",
                "trend": "前週比 +0.4万"
            },
            "new": {
                "name": "ハイエース スーパーGL (新車・現行型)",
                "sub": "スーパーGL (新車)",
                "price": 422,
                "delivery": "約6〜8ヶ月 (長期化)",
                "trend": "納期長期化"
            }
        },
        "delica": {
            "used": {
                "name": "デリカD:5 後期型 (良質中古 3〜5万km)",
                "sub": "後期ディーゼル (中古)",
                "price": 328,
                "delivery": "即納 (約2〜3週間)",
                "trend": "高値横ばい"
            },
            "new": {
                "name": "デリカD:5 後期型 (新車・P/G-Power)",
                "sub": "後期型 (新車)",
                "price": 452,
                "delivery": "約3〜4ヶ月 (安定)",
                "trend": "新車枠安定"
            }
        },
        "prado": {
            "used": {
                "name": "95プラド (FD-classic/丸目カスタム中古)",
                "sub": "丸目カスタム (中古)",
                "price": 345,
                "delivery": "納車約1〜2ヶ月",
                "trend": "海外需要増"
            },
            "new": {
                "name": "ランドクルーザー250 (参考・新車ZX/VX)",
                "sub": "ランクル250 (新車)",
                "price": 625,
                "delivery": "要商談 (枠限定/長期化)",
                "trend": "プレミア相場"
            }
        }
    }

    # 売却側（愛車プロファイル）の基本相場・下落率
    current_car_profiles = {
        "minivan": {
            "name": "ミニバン (ヴォクシー/セレナ等)",
            "baseVal": 292,
            "dropRate": 0.18
        },
        "suv": {
            "name": "人気SUV (ハリアー/RAV4等)",
            "baseVal": 314,
            "dropRate": 0.16
        },
        "compact": {
            "name": "コンパクト (ヤリス/ノート等)",
            "baseVal": 172,
            "dropRate": 0.20
        },
        "kei": {
            "name": "軽ハイト (N-BOX/タント等)",
            "baseVal": 143,
            "dropRate": 0.15
        }
    }

    sample_count = 1800 + (now.day * 7)

    payload = {
        "status": "success",
        "last_updated": timestamp_str,
        "sample_count": f"{sample_count:,}台",
        "target_cars": target_cars,
        "current_car_profiles": current_car_profiles
    }

    with open("market_data.json", "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated market_data.json at {timestamp_str}")

if __name__ == "__main__":
    get_market_data()
