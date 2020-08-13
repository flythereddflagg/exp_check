  <h1>Exp Check</h1>



  <!-- The actual snackbar -->

    <div id="toast">Error:</div>



  <button id="clear data button">Clear Data</button>

  <button id="add food button">Add Food</button>

  <button id="delete food button">Delete Food</button> <br>

  <label for="search bar">Search: </label>

  <input type="text" id="search bar">

  <label for="sorter">Sort By: </label>

  <select id="sorter">

​    <option value="food name">Food Name</option>

​    <option value="add date">Date Added</option>

​    <option value="exp date">Expiration Date</option>

   </select><br>



    <table id="food data table">

​    <thead>

​      <tr>

​        <th>Food Name</th>

​        <th>Date Added</th>

​        <th>Expiration Date</th>

​      </tr>

​    </thead>

​    <tbody id="food data"> </tbody>

  </table>

</body>

<script type="module" src="js/index.js"></script>

