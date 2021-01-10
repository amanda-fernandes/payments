const form = document.getElementById('cc-form');
const holder = document.getElementById('holder');
const card = document.getElementById('cc-number');
const exp_date = document.getElementById('exp_date');
const cvv = document.getElementById('cvv');
const brand = document.getElementById('brand');


form.addEventListener('submit', (event) => {
    event.preventDefault();
    if(validateHolder() && validateCreditCard() && validateCVV()) {
        creditCardBrand(card,brand);     
                   
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
    if (!meetLength(card, 16, 17)) return;
    return true;
}

function validateCVV() {
    if (checkIfEmpty(cvv)) return;
    if (!containsCharacters(cvv,2)) return;    
    if (!meetLength(cvv, 3, 4)) return;
    return true;
}

async function creditCardBrand(fieldCard,fieldBrand){   
    let cc = fieldCard.value.toString();
    console.log(cc);
    let data = { "cc_number":  cc};    
    let url = "/v1/credit-card-validation";
    await postData(url,data)
        .then(data => {
            if(data['brand'])
            {
                fieldBrand.value = data["brand"];
                  
                let dataSubmit = { 
                    "cc_number": card.value,            
                    "exp_date": exp_date.value,
                    "holder": holder.value,
                    "cvv": cvv.value
                };  

                let url = "/v1/credit-card";
                postData(url,dataSubmit)
                    .then(data => {
                        console.log(data);
                    });             
            }
        });  
}





