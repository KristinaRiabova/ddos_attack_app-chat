function launchAttack() {
  var target = document.getElementById("target").value;
  var numRequests = document.getElementById("requests").value;


  console.log("Launching attack with target:", target, "and number of requests:", numRequests);

  fetch("/launch_attack/", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded", 
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body:
      "target=" +
      encodeURIComponent(target) +
      "&requests=" +
      encodeURIComponent(numRequests), 
  })
    .then((response) => {
      if (response.ok) {
        alert("Attack launched successfully!");
      } else {
        alert("Error launching attack.");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("Error launching attack.");
    });
}


function toggleMenu() {
  var menu = document.getElementById("menu");
  if (menu.style.display === "block") {
    menu.style.display = "none";
    console.log("Menu is hidden");
  } else {
    menu.style.display = "block";
    console.log("Menu is displayed");
  }
}


function toggleTheme() {
  var body = document.body;
  var hackerIcon = document.querySelector(".hacker-icon");
  var menuIcon = document.querySelector(".menu-icon");
  var themeIcon = document.querySelector(".theme-icon");
  var container = document.querySelector(".container");

  if (body.classList.contains("dark-theme")) {
    body.classList.remove("dark-theme");
    body.classList.add("light-theme");
    hackerIcon.style.color = "#222121";
    menuIcon.style.color = "#222121";
    themeIcon.classList.remove("fa-sun");
    themeIcon.classList.add("fa-moon");
    themeIcon.style.color = "#000000";
    container.style.backgroundColor = "#ffffff";
    console.log("Switched to light theme");
  } else {
    body.classList.remove("light-theme");
    body.classList.add("dark-theme");
    hackerIcon.style.color = "#34eb9e";
    menuIcon.style.color = "#34eb9e";
    themeIcon.classList.remove("fa-moon");
    themeIcon.classList.add("fa-sun");
    themeIcon.style.color = "#34eb9e";
    container.style.backgroundColor = "#575757";
    console.log("Switched to dark theme");
  }
}


function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(
          cookie.substring(name.length + 1)
        );
        break;
      }
    }
  }
  return cookieValue;
}
