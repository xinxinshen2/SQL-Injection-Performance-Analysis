<?php
// config.php
$servername = "localhost";
$db_username = "root";
$db_password = ""; // Default XAMPP password is empty
$dbname = "sql_test_db";

$conn = new mysqli($servername, $db_username, $db_password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>