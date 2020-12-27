const form = document.getElementById('cc-form');
const holder = document.getElementById('holder');
const card = document.getElementById('cc-number');
const exp_date = document.getElementById('exp_date');
const cvv = document.getElementById('cvv');

form.addEventListener('submit', function(event) {
    event.preventDefault();
    if(validateHolder() && validateCreditCard() && validateCVV()) {
        alert("VALIDATED!");
        
    }
    else
    {

    }
});

function validateHolder() {
    if (checkIfEmpty(holder)) return;
    if (!containsCharacters(holder,1)) return;
    if (!meetLength(holder, 2, 200)) return;
    return true;
}

function validateCreditCard() {
    if (checkIfEmpty(card)) return;
    if (!containsCharacters(card,2)) return;    
    if (!meetLength(card, 16, 16)) return;
    return true;
}

function validateCVV() {
    if (checkIfEmpty(cvv)) return;
    if (!containsCharacters(cvv,2)) return;    
    if (!meetLength(cvv, 3, 4)) return;
    return true;
}

/*window.onload = function(){ 
    const input_credit_card = document.getElementById('cc-number');               
    input_credit_card.addEventListener('keyup', event => {            
        console.log(input_credit_card);
        if(input_credit_card.length == 16)
        {
            let cc_number = input_credit_card;
            let data = { cc_number };
            let url = "/v1/credit-card-validation";
            postData(url,data)
                .then(data => {
                    console.log(data);
                    if(data.message == "200") 
                    {
                        
                    }
                });              
        }
        else 
        {

        }
    });
}*/


