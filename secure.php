<?php
// secure.php
include 'config.php';

$username = $_GET['username'] ?? '';
$message = "";

if ($username) {
    // SECURITY: Using a placeholder (?) for the parameter
    $stmt = $conn->prepare("SELECT * FROM users WHERE username = ?");
    
    // Bind the variable to the placeholder (s = string)
    $stmt->bind_param("s", $username);
    
    // Execute
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        $user = $result->fetch_assoc();
        $message = "Login Successful! Welcome, " . htmlspecialchars($user['username']);
    } else {
        $message = "Login Failed";
    }
    $stmt->close();
}
?>
<!DOCTYPE html>
<html>
<body>
    <h2>Secure Login</h2>
    <p>Status: <b><?php echo $message; ?></b></p>
</body>
</html>