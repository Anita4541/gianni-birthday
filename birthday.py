<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Happy Birthday, Gianni! 🎂🎶🎈</title>
    <style>
        body {
            background-color: pink;
            text-align: center;
            font-family: Arial, sans-serif;
        }
        h1 {
            color: #ff4081;
            font-size: 3rem;
            font-weight: bold;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
        }
        p {
            color: #d81b60;
            font-size: 1.5rem;
        }
        .music-btn {
            background-color: #ff4081;
            color: white;
            border: none;
            padding: 15px;
            font-size: 1.2rem;
            cursor: pointer;
            border-radius: 8px;
        }
        .music-btn:hover {
            background-color: #d81b60;
        }
        .emoji {
            font-size: 2rem;
            display: inline-block;
            margin: 10px;
        }
    </style>
</head>
<body>
    <h1>🎂 Tanti auguri a te, Gianni! 🎶🎈</h1>
    <p>Tanti auguri a te! 希望我们越来越好！ 🎉</p>
    
    <!-- 直接使用 Bensound 的音乐外链 -->
    <audio id="birthday-song" controls>
        <source src="https://www.bensound.com/bensound-music/bensound-happyrock.mp3" type="audio/mpeg">
        您的浏览器不支持音频播放。
    </audio>

    <button class="music-btn" onclick="document.getElementById('birthday-song').play()">🎵 点击播放生日快乐歌 🎵</button>

    <script>
        document.getElementById('birthday-song').onended = function() {
            alert("🎂 生日快乐, Gianni! 🎶🎈");
        };
    </script>
</body>
</html>
