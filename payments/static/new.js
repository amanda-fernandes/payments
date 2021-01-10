const form = document.getElementById('cc-form');
const holder = document.getElementById('holder');
const card = document.getElementById('cc-number');
const exp_date = document.getElementById('exp_date');
const cvv = document.getElementById('cvv');
const brand = document.getElementById('brand');
const notification = document.getElementById('notification');
const btn = document.getElementById("btn-submit"); 

form.addEventListener('submit', (event) => {
    event.preventDefault();
    if(btn.disabled == false) {
        let dataSubmit = { 
            "cc_number": card.value,            
            "exp_date": exp_date.value,
            "holder": holder.value,
            "cvv": cvv.value
        };  

        let url = "/v1/credit-card";
        postData(url,dataSubmit)
            .then(data => {
                if(data['message'] == "200"){
                    window.location.href = "/";
                }
                else{
                    notification.innerHTML = data['message'] + " <br/> Something went wrong. Please, try again!"
                }
            });      
                   
    }

});

function enableSubmit() 
{
    var qty = document.getElementsByClassName("is-success").length;
    if(qty = 5)
    {
        btn.disabled=false;
    }
}

function validateHolder() {
    if (checkIfEmpty(holder)) return;
    if (!containsCharacters(holder,1)) return;
    if (!meetLength(holder, 2, 200)) return;
    return true;
}

function validateCreditCard() {
    if (checkIfEmpty(card)) return;
    if (!containsCharacters(card,2)) return;    
    if (!meetLength(card, 10, 20)) return;
    getBrand(card, brand);
}

function validateCVV() {
    if (checkIfEmpty(cvv)) return;
    if (!containsCharacters(cvv,2)) return;    
    if (!meetLength(cvv, 3, 5)) return;
    return true;
}

function validateExpDate() {
    dateFormat(exp_date);
    if(containsCharacters(exp_date,4)) return;  
    return true;
}

async function getBrand(fieldCard,fieldBrand)
{
    let cc = fieldCard.value.toString();
    let data = { "cc_number":  cc};  
    let url = "/v1/credit-card-validation";
    await postData(url,data).then(data => {
        if(data['brand'])
        {
            fieldBrand.value = data["brand"];
            fieldBrand.classList.add("is-success");               
        }
        else
        {
            notification.innerHTML = data['message']; 
            setInvalid(card, `${card.name} not Validated`);           
        }
    });
}




