function addToCart(product, price) {
    const cartItems = JSON.parse(localStorage.getItem('cart')) || [];
    cartItems.push({ product, price });
    localStorage.setItem('cart', JSON.stringify(cartItems));
    alert(`${product} added to cart.`);
}

function buyNow(product, price) {
    localStorage.setItem('cart', JSON.stringify([{ product, price }]));
    window.location.href = 'thankyou.html';
}

document.addEventListener('DOMContentLoaded', () => {
    const cartTable = document.getElementById('cartTable');

    if (cartTable) {
        const tbody = cartTable.querySelector('tbody');
        const cartItems = JSON.parse(localStorage.getItem('cart')) || [];

        cartItems.forEach(item => {
            const row = document.createElement('tr');

            row.innerHTML = `
                <td>${item.product}</td>
                <td>$${item.price}</td>
                <td><button onclick="buyNow('${item.product}', ${item.price})">Buy Now</button></td>
            `;

            tbody.appendChild(row);
        });
    }
});