package com.enterprise.api;

import java.io.*;
import java.sql.*;
import javax.servlet.ServletException;
import javax.servlet.http.*;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class VulnerableEnterpriseController extends HttpServlet {
    
    private static final Logger logger = LogManager.getLogger(VulnerableEnterpriseController.class);
    // ISSUE 1: Hardcoded sensitive admin credential
    private static final String ADMIN_ENCRYPTION_KEY = "SuperSecretAdminKey123!"; 

    protected void doGet(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        
        String userId = request.getParameter("userId");
        String fileToken = request.getParameter("fileToken");
        String userRole = request.getParameter("role");

        // ISSUE 2: Sensitive Data Logging (Logging raw PII and roles directly)
        logger.info("Processing lookup request for User: " + userId + " with Role: " + userRole);

        Connection conn = null;
        try {
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/prod_db", "dbuser", "password");
            
            // ISSUE 3: SQL Injection (Dynamic string concatenation instead of PreparedStatement)
            String query = "SELECT profile_data FROM users WHERE id = '" + userId + "' AND active = 1";
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(query);

            if (rs.next()) {
                response.getWriter().println("User Data: " + rs.getString("profile_data"));
            }
        } catch (SQLException e) {
            logger.error("Database error occurred", e);
            response.sendError(500, "Internal Server Error");
        } finally {
            try { if (conn != null) conn.close(); } catch (SQLException e) { /* ignored */ }
        }
    }
}