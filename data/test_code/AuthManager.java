package com.enterprise.assets;

import java.io.*;
import javax.servlet.ServletException;
import javax.servlet.http.*;

public class EnterpriseAssetManager extends HttpServlet {

    protected void doPost(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        
        String reportType = request.getParameter("reportType");
        String userFilename = request.getParameter("filename");
        String outputFormat = request.getParameter("format");

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        // =========================================================================
        // ISSUE 1: Reflected Cross-Site Scripting (XSS) (CWE-79) - High
        // Directly writing raw, unencoded user input straight into the HTML DOM response
        // =========================================================================
        out.println("<html><body><h3>Generating Report for: " + reportType + "</h3>");

        // =========================================================================
        // ISSUE 2: Path Traversal / Arbitrary File Read (CWE-22) - High
        // Concatenating untrusted filename strings directly into a file pathway 
        // allowing structural access via directory traversal characters (../../)
        // =========================================================================
        File templateFile = new File("/var/app/templates/" + userFilename);
        if (templateFile.exists()) {
            BufferedReader reader = new BufferedReader(new FileReader(templateFile));
            String line;
            while ((line = reader.readLine()) != null) {
                out.println(line);
            }
            reader.close();
        }

        // =========================================================================
        // ISSUE 3: OS Command Injection (CWE-78) - Critical
        // Passing unvalidated runtime user arguments directly into system execution shells 
        // allowing an attacker to append malicious sub-commands via shell metacharacters (; or &&)
        // =========================================================================
        try {
            String systemCommand = "/usr/local/bin/generate_report.sh " + outputFormat;
            // Running raw dynamic string directly through native runtime execution
            Process process = Runtime.getRuntime().exec(systemCommand);
            process.waitFor();
            
            out.println("<p>Status: Generation engine successfully finished execution.</p>");
        } catch (Exception e) {
            out.println("<p>Error running generator pipeline: " + e.getMessage() + "</p>");
        }

        out.println("</body></html>");
    }
}