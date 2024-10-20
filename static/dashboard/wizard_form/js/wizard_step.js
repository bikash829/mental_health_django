class CloneFields{
    constructor(formFields,btnAdd,heading){
        /*
        (required parameter
        - form-field class every field
        - add button
        - parameter name
        )
        1. add more field object.formClone(counter)

        */
        this.formFields = formFields;
        this.btnAdd = btnAdd;
        this.heading = heading;
        this.counter = 0;
    }

    //method for field clone
    fieldClone(counter){
        const formInput = this.formFields.clone();

        for (let i = 0; i < formInput.find('.form-field').length; i++) {
            if(formInput.find('.form-field')[i].type == 'checkbox') {
                let inputField, inputLabel, generatedId;

                inputField = formInput.find('.form-field')[i];
                inputLabel = $(formInput.find('.form-field')[i]).siblings(`[for="${formInput.find('.form-field')[i].id}"]`)[0];
                generatedId = `${inputField.id}${counter}`;


                $(inputField).attr("id", generatedId);
                $(inputLabel).attr("for", generatedId);

                inputField.checked = false;

            }else if(formInput.find('.form-field')[i].disabled){
               $(formInput.find('.form-field')[i]).removeAttr('disabled');
               $(formInput.find('.form-field')[i]).attr('required','');

            }else{

                formInput.find('.form-field')[i].value = '';
            }
        }

        return formInput;
    }


    formClone(counter = 0){
        let newBlock = this.fieldClone(counter).clone().insertBefore(this.btnAdd[0].parentElement);
        $(newBlock).prepend(`
            <div class="position-relative pe-3 mb-3">
                ${this.heading}
                <button type="button" class="btn-close position-absolute top-0 end-0 pe-4 text-danger" aria-label="Close"></button>
            </div>
        `);
        $(newBlock).prepend('<hr class="my-5">');
    }
}// class end



class FormOperation{

    /*
        1. formElements property filter data by removing button element
        2. isEmpty property to validate empty form filed
        3. formElementList method element list in a map object
        4. repackedData method inputed data from user in a map object
        5. formDataPack property to get 3,4 both in a object
        6. formSlider form slider for save and continue

    */

    // constructor
    constructor(formArg,formContainer){
        this.formContainer  = formContainer;
        this.formElements = this.filteredElements(formArg);
        this.isEmpty = this.emptyValidation();
    }


    //filter data
    filteredElements(data){
        let rawData = data;

        const filterdItems =  [];

        [...rawData].forEach(item => {
            if(item.type !== "button" || item.type == "submit"){
                filterdItems.push(item);
            }
       })
       return filterdItems;
    }


    //empty validation function
    emptyValidation(){
        let isEmpty = false;

        const radioElement = [];
        const radioInput = new Map();

        this.formElements.forEach(( element, key ) => {
            if(element.type == "checkbox") {
                if(!(element.checked) && element.required ) {
                    isEmpty = true;
                }
            }else if(element.type == "radio"){
                radioElement.push(element);
            }else{
                if( element.value == "" ) {
                    if(element.required != false) {
                        isEmpty = true;
                    }
                }
            }
        });
        // radio button checker
        if(radioElement.length > 0){
            radioElement.forEach(radio => {
                if(!radioInput.has(radio.name)){
                    radioInput.set(radio.name,[]);
                    radioInput.get(radio.name).push(radio);
                }else{
                    radioInput.get(radio.name).push(radio);
                }
            });

            radioInput.forEach(items => {
                if(items.length > 0){
                    let radioCheker = false;
                    items.forEach(item => {
                        if(item.checked){
                            radioCheker = true;
                        }
                    });

                    if(!radioCheker){
                        isEmpty = true;
                    }
                }
            });
        }

        return isEmpty;
    }


    //form elements list
    formElementList(){
        const data = new Map();
        const dataArray = [];
        // let count = 1;


        this.formElements.forEach(element =>{
            if(element.type == 'radio' && !element.checked){
                return;
            }
            if(data.has(element.name)){
                dataArray.push(new Map(data));
                data.clear();
            }
            data.set(element.name,element);

        })

        if(dataArray.length < 1){
            return data;
        }else{
            dataArray.push(new Map(data));
            return dataArray;
        }
    }


    //final data packaging
    repackedData(){
        const data = new Map();
        const dataArray = [];


        this.formElements.forEach(element => {
            //radio button cheker
            if(element.type == 'radio' && !element.checked){
                return;
            }
            if(data.has(element.name)){
                dataArray.push(new Map(data));
                data.clear();
            }
            if(element.type == "file"){
                // element.files["file_path"] = element.value;
                // data.set(element.name,element.files);
                // pass;

            }else{
                if(element.type == 'checkbox'){
                    data.set(element.name,element.checked);
                }else{

                    data.set(element.name,element.value);

                }
            }
        })


        if(dataArray.length < 1){
            return data;
        }else{
            dataArray.push(new Map(data));
            return dataArray;
        }
        // return data;
    }

    //data pack
    get formDataPack() {
        const data = {
            "repackedData": this.repackedData(),
            "dataElements": this.formElementList(),
        }

        return data;
    }

    //show hide from
    formSlider(show){
        this.formContainer.hide(0,()=>show.show());
    }

}//edn class from validation






