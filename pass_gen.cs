using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Security.Cryptography;
using System.Text;

class PassGen
{
    public static string Main(string[] args, int length)
    {
        var charcount = new Random();
        var list = new List<string> { "9", "10", "11", "12", "13", "14" };
        int index = charcount.Next(list.Count);
        var repeat = (list[index]);

        Int32.TryParse(repeat, out int val);
        Console.WriteLine("\nThis is val: " + val);

        var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&";
        StringBuilder res = new StringBuilder();
        using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
        {
            byte[] uintBuffer = new byte[sizeof(uint)];

            while (length-- > 0)
            {
                rng.GetBytes(uintBuffer);
                uint num = BitConverter.ToUInt32(uintBuffer, 0);
                res.Append(chars[(int)(num % (uint)chars.Length)]);

            }
        }
        return res.ToString();
    }
}