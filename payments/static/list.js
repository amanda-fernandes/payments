window.onload = (event) => {
    const tableRef = document.getElementById("cc_table");
    getData('/v1/credit-card').then(data => {
        const arr = data.message;
        for (let i = 0; i < arr.length; i++){
            const newRow = tableRef.insertRow(-1);
            let obj = arr[i];
            for (let key in obj){
                let value = obj[key]; 
                const newCell = newRow.insertCell(0);               
                let newText = document.createTextNode(value);
                newCell.appendChild(newText);
            }            
        }

       
    });

};