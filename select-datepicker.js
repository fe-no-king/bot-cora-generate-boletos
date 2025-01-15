

function converteData(date) {
    const meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ];

    const partes = date.split("/");
    const mes = partes[1];
    const ano = partes[2];

    const nomeMes = meses[parseInt(mes) - 1];

    return nomeMes+" "+ano;
}

function next_verify_date(count, date_text, date) {
   
    count++;

    let current_text = document.getElementsByClassName('react-datepicker__current-month')[0].textContent;

    if(current_text == undefined || count == 20){
        return 0;
    }

    if(current_text == date_text){

        let day = date.split("/")[0];
        document.getElementsByClassName("react-datepicker__day--0"+day)[0].click();
        return 0;
    }
    
    document.getElementsByClassName('react-datepicker__navigation--next')[0].click();

    setTimeout(() => {
        next_verify_date(count, date_text, date);
    }, 500);
}

next_verify_date(0, converteData('10/03/2024'), '10/03/2024');