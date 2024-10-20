class Validate{
    constructor(){
        // this.isAlphabetic = isAlphabetic;
    }

    isAlphabetic(arg){
        const pattern = /[^A-Za-z\s]+|^\s*$|\s{2,}|\t/g;
        if(pattern.test(arg)){
            return false;
        }else{
            return true;
        }
    }
}