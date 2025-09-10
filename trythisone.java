import java.util.Base64;

public class PrintFlag {
    public static void main(String[] args) {
        // Obfuscated Base64 parts (correct parts stored in obscure-looking Base64)
        String p1 = "ZmxhZ3tUSDM";      // "flag{TH3_" missing padding
        String p2 = "X0lTXw==";         // "_IS_"
        String p3 = "Rkw0Rw==";         // "FL4G"
        String p4 = "X1I0SFVMfQ==";     // "_R4HUL}"

        // Fake flags (some with misleading Base64 content)
        String fakeA = "ZmFrZV9mbGFnX2hlcmU="; // "fake_flag_here"
        String fakeB = "c29tZV9yYW5kb21fdGV4dA=="; // "some_random_text"
        String fakeC = "ZmxhZ3tOT1RfVEhJU19OT19GTkN9"; // "flag{NOT_THIS_NO_FNC}"
        String fakeD = "flag{TRY_THIS_ONE}";

        // Decoding real parts using extra logic to hide intentions
        String real1 = decode(p1);
        String real2 = decode(p2);
        String real3 = decode(p3);
        String real4 = decode(p4);

        // Combine the parts to form the final flag
        String flag = real1 + real3 + real2 + real4;

        // Print only the correct flag
        System.out.println(flag);
    }

    // A method to decode Base64 after adding missing padding if needed
    private static String decode(String encoded) {
        while (encoded.length() % 4 != 0) {
            encoded += "="; // Add padding if necessary
        }
        return new String(Base64.getDecoder().decode(encoded));
    }
}
