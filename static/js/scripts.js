copyLink1 = ()=>{
document.getElementById("imagelink").select();
document.execCommand("Copy");
}
copyLink =(element) => {
     document.getElementById(element).select();
     document.execCommand("copy");
            }