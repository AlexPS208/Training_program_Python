let toFirst = document.querySelector('#toFirst');
let toSecond = document.querySelectorAll('#toSecond');
let toThird = document.querySelector('#toThird');

let first = document.querySelector('.overlapse1');
let second = document.querySelector('.overlapse2');
let third = document.querySelector('.overlapse3');

let open_overflow = document.querySelector('.example_button');
let close_overflow = document.querySelectorAll('.close');

open_overflow.addEventListener('click', function () {
    first.style.display = 'grid';
    second.style.display = 'none';
    third.style.display = 'none';
});

close_overflow[0].addEventListener('click', function () {
    first.style.display = 'none';
    second.style.display = 'none';
    third.style.display = 'none';
});

close_overflow[1].addEventListener('click', function () {
    first.style.display = 'none';
    second.style.display = 'none';
    third.style.display = 'none';
});

close_overflow[2].addEventListener('click', function () {
    first.style.display = 'none';
    second.style.display = 'none';
    third.style.display = 'none';
});

toFirst.addEventListener('click', function () {
    first.style.display = 'grid';
    second.style.display = 'none';
    third.style.display = 'none';
});

toSecond[0].addEventListener('click', function () {
    first.style.display = 'none';
    second.style.display = 'grid';
    third.style.display = 'none';
});

toSecond[1].addEventListener('click', function () {
    first.style.display = 'none';
    second.style.display = 'grid';
    third.style.display = 'none';
});

toThird.addEventListener('click', function () {
    first.style.display = 'none';
    second.style.display = 'none';
    third.style.display = 'grid';
});

