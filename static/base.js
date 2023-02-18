window.onscroll = function() {
    const navbar = document.getElementById("navbar");
    if (window.pageYOffset > 0) {
      navbar.classList.add("sticky");
    } else {
      navbar.classList.remove("sticky");
    }
  };
  
