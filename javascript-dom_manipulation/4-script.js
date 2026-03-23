document.getElementById('add_item').addEventListener('click', function () {
    const newElement = document.createElement('li');
    newElement.textContent = 'Item';
    const list = document.querySelector('.my_list');
    list.appendChild(newElement);
});
