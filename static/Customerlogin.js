const customerName = document.getElementById('Namee').value;
const customerDetails = document.getElementsByClassName('customer-details');
for (let i = 0; i < customerDetails.length; i++) {
    // Get the customer name from the current element
    const currentName = document.getElementById('Named').innerText;
  
    // If the current name matches the customer name input, set the background color to red
    if (currentName === customerName) {
      customerDetails[i].style.backgroundColor = 'red';
    }
  }