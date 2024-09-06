async function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (!file) {
        alert('Please select a file to upload.');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        const fileLink = document.getElementById('fileLink');

        if (response.ok) {
            fileLink.innerHTML = <><p>File uploaded successfully!</p><a href="${result.url}" target="_blank">Download File</a></>;
        } else {
            fileLink.innerHTML = <p>Error: ${result.message}</p>;
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while uploading the file.');
    }
}