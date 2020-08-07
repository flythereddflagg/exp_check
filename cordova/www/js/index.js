

// Wait for the deviceready event before using any of Cordova's device APIs.
// See https://cordova.apache.org/docs/en/latest/cordova/events/events.html#deviceready
document.addEventListener('deviceready', onDeviceReady, false);
console.log(document.getElementById('table121'))
document.getElementById('table121').onclick = table_on_click

function onDeviceReady() {
    // Cordova is now initialized. Have fun!

    console.log('Running cordova-' + cordova.platformId + '@' + cordova.version);
    document.getElementById('deviceready').classList.add('ready');
}

function table_on_click() 
{
  var tbl_ptr = document.getElementById('table121');
  tbl_ptr.addClass('selected').siblings().removeClass('selected');
  var value = this.find('td:first').html();
  // alert(value);    
}


