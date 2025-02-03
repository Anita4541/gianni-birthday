<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Happy Birthday, Gianni! 🎂🎶🎈</title>
    <style>
        body {
            background: linear-gradient(45deg, #ff9a9e, #fad0c4, #fad0c4, #ffdde1);
            background-size: 400% 400%;
            animation: gradientBG 10s ease infinite;
            text-align: center;
            font-family: Arial, sans-serif;
            overflow: hidden;
            position: relative;
        }
        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        h1 {
            color: #ff4081;
            font-size: 3rem;
            font-weight: bold;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            margin-top: 50px;
        }
        p {
            color: #d81b60;
            font-size: 1.5rem;
        }
        .music-btn {
            background-color: #ff4081;
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 1.2rem;
            cursor: pointer;
            border-radius: 8px;
            margin-top: 20px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
            transition: transform 0.2s;
        }
        .music-btn:hover {
            background-color: #d81b60;
            transform: scale(1.1);
        }
        audio {
            margin-top: 20px;
            width: 80%;
        }
        /* 🎂 蜡烛样式 */
        .cake-container {
            position: relative;
            display: inline-block;
            margin-top: 20px;
        }
        .cake {
            width: 150px;
        }
        .candle {
            position: absolute;
            width: 30px;
            top: 10px;
            left: 50%;
            transform: translateX(-50%);
            transition: opacity 1s ease;
        }
        .candle-blown {
            opacity: 0;
        }
        /* 🎂🎶🎈 滚动动画 */
        .floating-emoji {
            font-size: 2rem;
            position: absolute;
            animation: floatUp 4s linear infinite;
        }
        @keyframes floatUp {
            0% { transform: translateY(100vh); opacity: 1; }
            100% { transform: translateY(-10vh); opacity: 0; }
        }
    </style>
</head>
<body>
    <h1>🎂 Tanti auguri a te, Gianni! 🎶🎈</h1>
    <p>Tanti auguri a te! 希望我们越来越好！ 🎉</p>

    <!-- 生日蛋糕 + 蜡烛 -->
    <div class="cake-container">
        <img id="candle" class="candle" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Candle_flame.svg/40px-Candle_flame.svg.png">
        <img id="cake" class="cake" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Birthday_cake.svg/200px-Birthday_cake.svg.png" onclick="blowCandle()">
    </div>

    <!-- 音乐 -->
    <audio id="birthday-song" controls>
        <source src="https://www.bensound.com/bensound-music/bensound-happyrock.mp3" type="audio/mpeg">
        您的浏览器不支持音频播放。
    </audio>

    <button class="music-btn" onclick="document.getElementById('birthday-song').play()">🎵 点击播放生日快乐歌 🎵</button>

    <script>
        document.getElementById('birthday-song').onended = function() {
            alert("🎂 生日快乐, Gianni! 🎶🎈");
        };

        function blowCandle() {
            let candle = document.getElementById("candle");
            candle.classList.add("candle-blown");
            alert("🎂 你吹灭了蜡烛！许个愿吧！🎉");
        }

        function createFloatingEmoji() {
            const emojis = ["🎂", "🎶", "🎈"];
            const emoji = document.createElement("div");
            emoji.className = "floating-emoji";
            emoji.innerText = emojis[Math.floor(Math.random() * emojis.length)];
            emoji.style.position = "absolute";
            emoji.style.left = Math.random() * 100 + "vw";
            emoji.style.top = "100vh";
            emoji.style.fontSize = "2rem";
            emoji.style.animation = "floatUp " + (Math.random() * 3 + 2) + "s linear infinite";
            document.body.appendChild(emoji);

            setTimeout(() => {
                emoji.remove();
            }, 4000);
        }
        setInterval(createFloatingEmoji, 500);
    </script>
</body>
</html>
