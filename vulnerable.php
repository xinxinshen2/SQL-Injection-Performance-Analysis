<?php
// vulnerable.php
include 'config.php';

$username = $_GET['username'] ?? '';
$message = "";

if ($username) {
    // VULNERABILITY: Directly concatenating input into the query string
    $sql = "SELECT * FROM users WHERE username = '$username'";
    
    // Execute query
    $result = $conn->query($sql);

    if ($result && $result->num_rows > 0) {
        $user = $result->fetch_assoc();
        $message = "Login Successful! Welcome, " . htmlspecialchars($user['username']);
    } else {
        $message = "Login Failed";
    }
}
?>
<!DOCTYPE html>
<html>
<body>
    <h2>Vulnerable Login</h2>
    <p>Status: <b><?php echo $message; ?></b></p>
</body>
</html>