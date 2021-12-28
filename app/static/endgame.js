
function show_more() {
    additional_words = document.getElementById("words-list-hidden")
    additional_words.style.display = "inline"
    show_less_btn = document.getElementById("show-less-btn")
    show_less_btn.style.display = "inline"
    show_more_btn = document.getElementById("show-more-btn")
    show_more_btn.style.display = "none"
}

function show_less() {
    additional_words = document.getElementById("words-list-hidden")
    additional_words.style.display = "none"
    show_less_btn = document.getElementById("show-less-btn")
    show_less_btn.style.display = "none"
    show_more_btn = document.getElementById("show-more-btn")
    show_more_btn.style.display = "inline"
}