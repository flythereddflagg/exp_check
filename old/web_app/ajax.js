function loadDoc() {
  var xhttp = new XMLHttpRequest();
  console.log("1");
  xhttp.onreadystatechange = function() {
    console.log("2");
    if (this.readyState == 4 && this.status == 200) {
     console.log('3')
     document.getElementById("demo").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "ajax_info.txt", true);
  xhttp.send();
}