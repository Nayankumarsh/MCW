let deleteB = document.querySelector('#delete-btn');
      deleteB.addEventListener('click', () => {
        fetch('/customers/delete', { method: 'DELETE' })
          .then(response => {
            if (response.ok) {
              window.location.href = '/Manager';
            } else {
              console.log('Error deleting customers');
            }
          });
      });

//       const addCustomerForm = document.querySelector('#adde');
//       const customersList = document.querySelector('#tableBody');
      
//       addCustomerForm.addEventListener('submit', event => {
//         event.preventDefault();
      
//         const nameInput = document.querySelector('#title');
//         const phoneInput = document.querySelector('#Description');
      
//         fetch('/Manager', {
//           method: 'POST',
//           body: new FormData(addCustomerForm),
//         })
//         .then(response => {
//           if (response.ok) {
//             return response.json();
//           } else {
//             throw new Error('Failed to add customer');
//           }
//         })
//         .then(data => {
//           const customerItem = document.createElement('tr');
//           customerItem.innerHTML = `
//             <td>${data.Name}</td>
//             <td>${data.Phone}</td>
//             <td>${data.date}</td>
//             <td>
//               <a href="/Update/${data.SNo}" id="Update" type="button">Update</a>
//               <a href="/delete/${data.SNo}" id="Delete" type="button">Delete</a>
//             </td>
//           `;
//           customersList.appendChild(customerItem);
//           nameInput.value = '';
//           phoneInput.value = '';
//         })
//         .catch(error => {
//           console.log(error);
//         });
//       });
      