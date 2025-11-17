// source/js/duration.js
!(function() {
  // 1. 这里改成你的网站“生日”
  var start = new Date("2025/02/14 00:13:00");

  function pad(num) {
    return num.toString().padStart(2, "0");
  }

  function update() {
    var now = new Date();
    var diff = now - start; // 毫秒

    var days = Math.floor(diff / (1000 * 60 * 60 * 24));
    var hours = Math.floor(diff / (1000 * 60 * 60)) - days * 24;
    var minutes = Math.floor(diff / (1000 * 60)) - days * 24 * 60 - hours * 60;
    var seconds = Math.floor(diff / 1000) - days * 24 * 60 * 60 - hours * 60 * 60 - minutes * 60;

    // 2. 下面两句可以按你想要的句式改
    var timeDateEl = document.getElementById("timeDate");
    var timesEl = document.getElementById("times");
    if (!timeDateEl || !timesEl) return;

    // timeDateEl.innerHTML = "本站已记录我&nbsp;" + days + "&nbsp;天";
    // timesEl.innerHTML =
    //   "&nbsp;" + pad(hours) + "&nbsp;小时&nbsp;" +
    //   pad(minutes) + "&nbsp;分&nbsp;" +
    //   pad(seconds) + "&nbsp;秒的生活";
    // 更专业的文案：由 footer 的 HTML 负责前后文字，这里只填“时间部分”
    timeDateEl.textContent = days + " 天";
    timesEl.textContent =
      pad(hours) + " 小时 " +
      pad(minutes) + " 分 " +
      pad(seconds) + " 秒";
  }

  update();
  setInterval(update, 1000); // 每秒刷新一次
})();
