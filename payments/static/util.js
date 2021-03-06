function checkIfEmpty(field) {
    if (isEmpty(field.value.trim())) {      
      setInvalid(field, `${field.name} must not be empty`);
      return true;
    } else {    
      setValid(field);
      return false;
    }
}

function isEmpty(value) {
    if (value === '') return true;
    return false;
}

function setInvalid(field, message) {
    field.className = 'input is-danger';
    field.nextElementSibling.innerHTML = message;
    field.nextElementSibling.style.color = 'red';
}

function setValid(field) {
    field.className = 'input is-success';
    field.nextElementSibling.innerHTML = '';

}


function checkIfOnlyNumbers(field) {
    if (/(?=.*\d)/.test(field.value)) {
      setValid(field);
      return true;
    } else {
      setInvalid(field, `${field.name} must contain only numbers`);
      return false;
    }
}

function meetLength(field, minLength, maxLength) {
    if (field.value.length >= minLength && field.value.length < maxLength) {
      setValid(field);
      return true;
    } else if (field.value.length < minLength) {
      setInvalid(
        field,
        `${field.name} must be at least ${minLength} characters long`
      );
      return false;
    } else {
      setInvalid(
        field,
        `${field.name} must be shorter than ${maxLength} characters`
      );
      return false;
    }
}

function containsCharacters(field, code) {
    let regEx;
    switch (code) {
      case 1:
        // letters
        regEx = /(?=.*[a-zA-Z])/;
        return matchWithRegEx(regEx, field, 'Must contain only letters');
      case 2:
        // numbers
        regEx = /^\d+$/;
        return matchWithRegEx(
          regEx,
          field,
          'Must contain only numbers'
        );
      case 3:
        // Email pattern
        regEx = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return matchWithRegEx(regEx, field, 'Must be a valid email address');
      case 4:
        //YYYY/MM
        regEx = /^\d{4}\/\d{2}$/;
        return matchWithRegEx(regEx, field, 'Must be a YYYY/MM');
      default:
        return false;
    }
}

function matchWithRegEx(regEx, field, message) {
    if (field.value.match(regEx)) {
      setValid(field);
      return true;
    } else {
      setInvalid(field, message);
      return false;
    }
}

function dateFormat(el){
    value = el.value;       
    el.value = value.replace(/^([\d]{4})([\d]{2})$/,"$1/$2");          
}

async function postData(url = '', data = {}) 
{
    const response = await fetch(url, {
        method: 'POST', 
        mode: 'cors', 
        cache: 'no-cache', 
        credentials: 'same-origin',
        headers: {
        'Content-Type': 'application/json'            
        },
        redirect: 'follow', 
        referrerPolicy: 'no-referrer', 
        body: JSON.stringify(data) 
    });
    return response.json(); 
}

async function getData(url = '') 
{
    const response = await fetch(url, {
        method: 'GET', 
        mode: 'cors', 
        cache: 'no-cache', 
        credentials: 'same-origin',
        headers: {
        'Content-Type': 'application/json'            
        },
        redirect: 'follow', 
        referrerPolicy: 'no-referrer'
    });
    return response.json(); 
}
