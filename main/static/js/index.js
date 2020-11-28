const dataInputForm=document.querySelector('form');
const loadingSpinner=document.querySelector('.loading');
const nameSpan=document.querySelector('.name');
const API_URL='/api/'


loadingSpinner.style.display="none";
dataInputForm.addEventListener('submit',(event)=>{
    const form_data= new FormData(dataInputForm);

    let name=form_data.get('name');
    let age=form_data.get('age');

    let dataObj={
        name:name,
        age:age
    }

    loadingSpinner.style.display="";
    dataInputForm.style.display="none";
    fetch(
        API_URL,
        {   method:"POST",
            body:JSON.stringify(dataObj),
            headers:{
                'content-type':'application/json',
            }
        }
    ).then(
        response=>{
            return response.json();
        })
     
       .then(data=>{
           dataInputForm.reset();
           console.log(data.student.name);
           dataInputForm.style.display="";
           nameSpan.innerHTML=data['student']['name'];
           loadingSpinner.style.display="none";
        })

    event.preventDefault();
}) 

