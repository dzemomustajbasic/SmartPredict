var btn = document.querySelector('.dropbtn');

function toggleDropdown() {
    console.log("TESTTT")
    var dropdownContent = document.querySelector('.dropdown-content');
    dropdownContent.classList.toggle('show');
    if (dropdownContent.classList.contains('show')) {
        btn.style.color = '#6f42c1';
    } else {
        btn.style.color = 'white';
    }
}

window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName('dropdown-content');
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
                btn.style.color = 'white';
            }
        }
    }
}

