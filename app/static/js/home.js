console.log("RADIM")

document.addEventListener("DOMContentLoaded", function() {
    var introModels = document.querySelector(".intro-models");
    var introDescription = document.querySelector(".intro-description")

    function checkVisibility() {
        var introModelsPosition = introModels.getBoundingClientRect().top;
        var introDescriptionPosition = introDescription.getBoundingClientRect().top
        var windowHeight = window.innerHeight;

        if(introDescriptionPosition < windowHeight) {
            console.log("IDE")
            introDescription.classList.add("show");
        }

        if (introModelsPosition < windowHeight) {
            console.log("USAO SAM OVDJE")
            introModels.classList.add("show");
        }
    }
    checkVisibility();

    window.addEventListener("scroll", function() {
        checkVisibility();
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var aiImage = document.querySelector(".ai-image");
    var aiTechniques = document.querySelector(".ai-techniques");

    function checkVisibility() {
        var aiImagePosition = aiImage.getBoundingClientRect().top;
        var aiTechniquesPosition = aiTechniques.getBoundingClientRect().top;
        var windowHeight = window.innerHeight;

        if (aiImagePosition < windowHeight) {
            aiImage.classList.add("show");
        }

        if (aiTechniquesPosition < windowHeight) {
            aiTechniques.classList.add("show");
        }
    }

    window.addEventListener("scroll", function() {
        checkVisibility();
    });

    checkVisibility();
});

document.addEventListener("DOMContentLoaded", function() {
    var workflowImage = document.querySelector(".workflow");
    console.log(workflowImage, "NESTO")

    function checkVisibility() {
        var workflowPosition = workflowImage.getBoundingClientRect().top;
        var windowHeight = window.innerHeight;

        if (workflowPosition < windowHeight) {
            console.log("ZADOVOLJEN USLOV")
            workflowImage.classList.add("showimg");
        }
    }

    window.addEventListener("scroll", function() {
        checkVisibility();
    });

    checkVisibility();
});
