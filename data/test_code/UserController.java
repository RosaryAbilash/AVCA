public class UserController {
    public void getUserData(String username) {
        String query = "SELECT * FROM users WHERE username = '" + username + "'";
        db.execute(query);
    }
}