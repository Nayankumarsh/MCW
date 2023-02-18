const deleteBtn = document.querySelector('#delete-btn');
      deleteBtn.addEventListener('click', () => {
        fetch('/workers/Wdelete', { method: 'DELETE' })
          .then(response => {
            if (response.ok) {
              window.location.href = '/Addworker';
            } else {
              console.log('Error deleting customers');
            }
          });
      });