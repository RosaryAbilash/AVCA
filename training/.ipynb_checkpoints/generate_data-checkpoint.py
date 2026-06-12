import json
import random
from pathlib import Path
from collections import Counter

OUTPUT_FILE = Path("dataset.jsonl")

INSTRUCTION = (
    "You are a senior enterprise security engineer. "
    "Fix all security vulnerabilities in the Java code. "
    "Preserve business logic. "
    "Return only secure, compile-ready Java code."
)

TABLE_NAMES = ["users", "employees", "accounts", "customers"]
COLUMN_NAMES = ["username", "email", "userid", "account_id"]
SECRET_NAMES = ["API_KEY", "DB_PASSWORD", "JWT_SECRET", "ADMIN_TOKEN"]
DOMAINS = ["example.com", "enterprise.internal", "api.company.com"]

# =========================================================================
# SINGLE VULNERABILITY GENERATORS
# =========================================================================

def sql_injection_example():
    table = random.choice(TABLE_NAMES)
    column = random.choice(COLUMN_NAMES)
    vulnerable = f"""
public class DatabaseDAO {{
    public boolean verifyRecord(String {column}) throws Exception {{
        String query =
        "SELECT * FROM {table} WHERE {column}='"
        + {column} +
        "'";
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery(query);
        return rs.next();
    }}
}}
"""
    fixed = f"""
public class DatabaseDAO {{
    public boolean verifyRecord(String {column}) throws Exception {{
        String query =
        "SELECT * FROM {table} WHERE {column}=?";
        PreparedStatement stmt = conn.prepareStatement(query);
        stmt.setString(1, {column});
        ResultSet rs = stmt.executeQuery();
        return rs.next();
    }}
}}
"""
    return vulnerable.strip(), fixed.strip()

def hardcoded_secret_example():
    secret_name = random.choice(SECRET_NAMES)
    vulnerable = f"""
public class ConfigManager {{
    private static final String {secret_name} = "SUPER_SECRET_123!@#";

    public String getSecret() {{
        return {secret_name};
    }}
}}
"""
    fixed = f"""
public class ConfigManager {{
    private static final String {secret_name} = System.getenv("{secret_name}");

    public String getSecret() {{
        if ({secret_name} == null) {{
            throw new IllegalStateException("Secret not configured");
        }}
        return {secret_name};
    }}
}}
"""
    return vulnerable.strip(), fixed.strip()

def path_traversal_example():
    vulnerable = """
public class FileService {
    public byte[] downloadFile(String filename) throws IOException {
        File file = new File("/var/app/uploads/" + filename);
        return Files.readAllBytes(file.toPath());
    }
}
"""
    fixed = """
public class FileService {
    public byte[] downloadFile(String filename) throws IOException {
        Path baseDir = Paths.get("/var/app/uploads");
        Path safePath = baseDir.resolve(filename).normalize();
        
        if (!safePath.startsWith(baseDir)) {
            throw new SecurityException("Invalid file path detected");
        }
        return Files.readAllBytes(safePath);
    }
}
"""
    return vulnerable.strip(), fixed.strip()

def command_injection_example():
    vulnerable = """
public class NetworkUtil {
    public void pingHost(String host) throws Exception {
        String cmd = "ping -c 4 " + host;
        Process process = Runtime.getRuntime().exec(cmd);
        process.waitFor();
    }
}
"""
    fixed = """
public class NetworkUtil {
    public void pingHost(String host) throws Exception {
        ProcessBuilder pb = new ProcessBuilder("ping", "-c", "4", host);
        Process process = pb.start();
        process.waitFor();
    }
}
"""
    return vulnerable.strip(), fixed.strip()

def logging_example():
    vulnerable = """
public class AuthService {
    private static final Logger logger = LoggerFactory.getLogger(AuthService.class);

    public void authenticate(String user, String password) {
        logger.info("Processing login for User=" + user + " Password=" + password);
        // Authentication logic
    }
}
"""
    fixed = """
public class AuthService {
    private static final Logger logger = LoggerFactory.getLogger(AuthService.class);

    public void authenticate(String user, String password) {
        logger.info("Processing login request");
        // Authentication logic
    }
}
"""
    return vulnerable.strip(), fixed.strip()

def weak_crypto_example():
    vulnerable = """
public class HashUtil {
    public byte[] generateHash(String input) throws Exception {
        MessageDigest md = MessageDigest.getInstance("MD5");
        return md.digest(input.getBytes());
    }
}
"""
    fixed = """
public class HashUtil {
    public byte[] generateHash(String input) throws Exception {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        return md.digest(input.getBytes());
    }
}
"""
    return vulnerable.strip(), fixed.strip()

def xss_example():
    vulnerable = """
public class SearchController extends HttpServlet {
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        String query = req.getParameter("q");
        resp.setContentType("text/html");
        PrintWriter out = resp.getWriter();
        out.println("<h1>Search Results for: " + query + "</h1>");
    }
}
"""
    fixed = """
public class SearchController extends HttpServlet {
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        String query = req.getParameter("q");
        resp.setContentType("text/html");
        PrintWriter out = resp.getWriter();
        // Using OWASP Java Encoder
        out.println("<h1>Search Results for: " + Encode.forHtml(query) + "</h1>");
    }
}
"""
    return vulnerable.strip(), fixed.strip()

def ssrf_example():
    domain = random.choice(DOMAINS)
    vulnerable = """
public class WebhookService {
    public void triggerWebhook(String targetUrl) throws Exception {
        URL url = new URL(targetUrl);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.connect();
    }
}
"""
    fixed = f"""
public class WebhookService {{
    public void triggerWebhook(String targetUrl) throws Exception {{
        URL url = new URL(targetUrl);
        if (!url.getHost().endsWith(".{domain}")) {{
            throw new SecurityException("Unauthorized webhook destination");
        }}
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.connect();
    }}
}}
"""
    return vulnerable.strip(), fixed.strip()

def insecure_deserialization_example():
    vulnerable = """
public class SessionManager {
    public UserProfile restoreSession(InputStream stream) throws Exception {
        ObjectInputStream in = new ObjectInputStream(stream);
        UserProfile profile = (UserProfile) in.readObject();
        in.close();
        return profile;
    }
}
"""
    fixed = """
public class SessionManager {
    public UserProfile restoreSession(String jsonPayload) throws Exception {
        ObjectMapper mapper = new ObjectMapper();
        return mapper.readValue(jsonPayload, UserProfile.class);
    }
}
"""
    return vulnerable.strip(), fixed.strip()

def ldap_injection_example():
    vulnerable = """
public class DirectoryService {
    public NamingEnumeration<SearchResult> findUser(DirContext ctx, String username) throws Exception {
        String filter = "(uid=" + username + ")";
        SearchControls controls = new SearchControls();
        controls.setSearchScope(SearchControls.SUBTREE_SCOPE);
        return ctx.search("ou=users,dc=enterprise,dc=com", filter, controls);
    }
}
"""
    fixed = """
public class DirectoryService {
    public NamingEnumeration<SearchResult> findUser(DirContext ctx, String username) throws Exception {
        String filter = "(uid={0})";
        SearchControls controls = new SearchControls();
        controls.setSearchScope(SearchControls.SUBTREE_SCOPE);
        Object[] filterArgs = new Object[]{username};
        return ctx.search("ou=users,dc=enterprise,dc=com", filter, filterArgs, controls);
    }
}
"""
    return vulnerable.strip(), fixed.strip()

def xxe_example():
    vulnerable = """
public class XmlProcessor {
    public Document parseXml(InputStream is) throws Exception {
        DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = dbf.newDocumentBuilder();
        return builder.parse(is);
    }
}
"""
    fixed = """
public class XmlProcessor {
    public Document parseXml(InputStream is) throws Exception {
        DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
        dbf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
        dbf.setFeature("http://xml.org/sax/features/external-general-entities", false);
        dbf.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
        dbf.setXIncludeAware(false);
        dbf.setExpandEntityReferences(false);
        
        DocumentBuilder builder = dbf.newDocumentBuilder();
        return builder.parse(is);
    }
}
"""
    return vulnerable.strip(), fixed.strip()

def unsafe_file_upload_example():
    vulnerable = """
public class UploadController {
    public void uploadAvatar(MultipartFile file) throws Exception {
        String filename = file.getOriginalFilename();
        File dest = new File("/app/avatars/" + filename);
        file.transferTo(dest);
    }
}
"""
    fixed = """
public class UploadController {
    public void uploadAvatar(MultipartFile file) throws Exception {
        String originalName = file.getOriginalFilename();
        if (originalName == null || !originalName.matches("^[a-zA-Z0-9_-]+\\\\.(jpg|png)$")) {
            throw new IllegalArgumentException("Invalid file type");
        }
        
        String safeName = UUID.randomUUID().toString() + "_" + originalName;
        File dest = new File("/app/avatars/" + safeName);
        file.transferTo(dest);
    }
}
"""
    return vulnerable.strip(), fixed.strip()

def open_redirect_example():
    vulnerable = """
public class RedirectController extends HttpServlet {
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        String url = req.getParameter("continue");
        resp.sendRedirect(url);
    }
}
"""
    fixed = """
public class RedirectController extends HttpServlet {
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        String url = req.getParameter("continue");
        if (url != null && url.startsWith("/") && !url.startsWith("//")) {
            resp.sendRedirect(url);
        } else {
            resp.sendRedirect("/home");
        }
    }
}
"""
    return vulnerable.strip(), fixed.strip()

def jwt_validation_example():
    vulnerable = """
public class JwtAuthenticator {
    public Claims decodeToken(String token) {
        // Parses token without validating the cryptographic signature
        return Jwts.parser()
                   .parseClaimsJwt(token)
                   .getBody();
    }
}
"""
    fixed = """
public class JwtAuthenticator {
    private Key signingKey; // Injected secure key
    
    public Claims decodeToken(String token) {
        // Cryptographically verifies signature and expiration
        Claims claims = Jwts.parserBuilder()
                   .setSigningKey(signingKey)
                   .build()
                   .parseClaimsJws(token)
                   .getBody();
                   
        if (claims.getExpiration() != null && claims.getExpiration().before(new Date())) {
            throw new SecurityException("Token expired");
        }
        return claims;
    }
}
"""
    return vulnerable.strip(), fixed.strip()

def missing_input_validation_example():
    vulnerable = """
public class TransactionService {
    public void processTransfer(String accountId, double amount) {
        Account target = accountRepo.findById(accountId);
        target.addBalance(amount);
        accountRepo.save(target);
    }
}
"""
    fixed = """
public class TransactionService {
    public void processTransfer(String accountId, double amount) {
        if (amount <= 0 || amount > 1000000) {
            throw new IllegalArgumentException("Transfer amount is out of valid bounds.");
        }
        if (accountId == null || accountId.trim().isEmpty()) {
            throw new IllegalArgumentException("Account ID must be provided.");
        }
        
        Account target = accountRepo.findById(accountId);
        target.addBalance(amount);
        accountRepo.save(target);
    }
}
"""
    return vulnerable.strip(), fixed.strip()

def sensitive_exception_leakage_example():
    vulnerable = """
public class ApiController {
    public Response handleRequest(Request req) {
        try {
            return processRequest(req);
        } catch (Exception e) {
            // Leaking internal stack traces and details to the user
            return new Response(500, "System failure: " + e.getMessage() + " Trace: " + Arrays.toString(e.getStackTrace()));
        }
    }
}
"""
    fixed = """
public class ApiController {
    private static final Logger logger = LoggerFactory.getLogger(ApiController.class);

    public Response handleRequest(Request req) {
        try {
            return processRequest(req);
        } catch (Exception e) {
            // Log full details internally, return generic message to user
            logger.error("System failure during request processing", e);
            return new Response(500, "An internal server error occurred. Please try again later.");
        }
    }
}
"""
    return vulnerable.strip(), fixed.strip()

# =========================================================================
# MULTI-VULNERABILITY GENERATORS
# =========================================================================

def multi_sqli_secret_logging():
    secret = random.choice(SECRET_NAMES)
    vulnerable = f"""
public class LegacyAuthDAO {{
    private static final String {secret} = "super_secret_db_pass";
    private static final Logger logger = LoggerFactory.getLogger(LegacyAuthDAO.class);

    public boolean authenticate(String username, String password) throws Exception {{
        logger.info("Attempting login: user=" + username + " pass=" + password);
        String query = "SELECT * FROM users WHERE username='" + username + "' AND active=1";
        Statement stmt = conn.createStatement();
        return stmt.executeQuery(query).next();
    }}
}}
"""
    fixed = f"""
public class LegacyAuthDAO {{
    private static final String {secret} = System.getenv("{secret}");
    private static final Logger logger = LoggerFactory.getLogger(LegacyAuthDAO.class);

    public boolean authenticate(String username, String password) throws Exception {{
        logger.info("Processing authentication request");
        String query = "SELECT * FROM users WHERE username=? AND active=1";
        PreparedStatement stmt = conn.prepareStatement(query);
        stmt.setString(1, username);
        return stmt.executeQuery().next();
    }}
}}
"""
    return vulnerable.strip(), fixed.strip()

def multi_xss_input_validation():
    vulnerable = """
public class ProfileServlet extends HttpServlet {
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        String bio = req.getParameter("bio");
        resp.setContentType("text/html");
        PrintWriter out = resp.getWriter();
        out.println("<div class='bio'>" + bio + "</div>");
    }
}
"""
    fixed = """
public class ProfileServlet extends HttpServlet {
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        String bio = req.getParameter("bio");
        if (bio == null || bio.length() > 1000) {
            throw new IllegalArgumentException("Bio exceeds maximum allowed length.");
        }
        resp.setContentType("text/html");
        PrintWriter out = resp.getWriter();
        out.println("<div class='bio'>" + Encode.forHtml(bio) + "</div>");
    }
}
"""
    return vulnerable.strip(), fixed.strip()

def multi_ssrf_input_validation():
    domain = random.choice(DOMAINS)
    vulnerable = """
public class ProxyController {
    public void fetchExternalResource(String urlParam) throws Exception {
        URL url = new URL(urlParam);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.connect();
    }
}
"""
    fixed = f"""
public class ProxyController {{
    public void fetchExternalResource(String urlParam) throws Exception {{
        if (urlParam == null || urlParam.trim().isEmpty()) {{
            throw new IllegalArgumentException("URL parameter cannot be empty");
        }}
        
        URL url = new URL(urlParam);
        if (!url.getHost().endsWith(".{domain}")) {{
            throw new SecurityException("Target domain is not whitelisted");
        }}
        
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.connect();
    }}
}}
"""
    return vulnerable.strip(), fixed.strip()

# =========================================================================
# PIPELINE CONFIGURATION
# =========================================================================

SINGLE_GENERATORS = [
    ("SQL Injection (CWE-89)", sql_injection_example),
    ("Hardcoded Secret (CWE-798)", hardcoded_secret_example),
    ("Path Traversal (CWE-22)", path_traversal_example),
    ("Command Injection (CWE-78)", command_injection_example),
    ("Sensitive Logging (CWE-532)", logging_example),
    ("Weak Cryptography (CWE-327)", weak_crypto_example),
    ("XSS (CWE-79)", xss_example),
    ("SSRF (CWE-918)", ssrf_example),
    ("Insecure Deserialization (CWE-502)", insecure_deserialization_example),
    ("LDAP Injection (CWE-90)", ldap_injection_example),
    ("XXE (CWE-611)", xxe_example),
    ("Unsafe File Upload (CWE-434)", unsafe_file_upload_example),
    ("Open Redirect (CWE-601)", open_redirect_example),
    ("JWT Validation Issues (CWE-347)", jwt_validation_example),
    ("Missing Input Validation (CWE-20)", missing_input_validation_example),
    ("Sensitive Exception Leakage (CWE-209)", sensitive_exception_leakage_example),
]

MULTI_GENERATORS = [
    ("Multiple (SQLi, Hardcoded Secret, Logging)", multi_sqli_secret_logging),
    ("Multiple (XSS, Missing Input Validation)", multi_xss_input_validation),
    ("Multiple (SSRF, Missing Input Validation)", multi_ssrf_input_validation)
]

def build_example():
    # 85% chance for a single vulnerability, 15% chance for a multi-vulnerability combo
    if random.random() < 0.70:
        category, generator = random.choice(SINGLE_GENERATORS)
    else:
        category, generator = random.choice(MULTI_GENERATORS)

    vulnerable, fixed = generator()
    
    return {
        "instruction": INSTRUCTION,
        "input": vulnerable,
        "output": fixed,
        "category": category
    }

def generate_dataset(num_examples=5000):
    stats = Counter()
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for _ in range(num_examples):
            example = build_example()
            stats[example["category"]] += 1
            f.write(json.dumps(example) + "\n")
    print(f"Generated {num_examples} examples -> {OUTPUT_FILE}")
    print("\nDataset Distribution:\n")

    for k, v in sorted(stats.items()):
        print(f"{k}: {v}")

if __name__ == "__main__":
    generate_dataset(5000)