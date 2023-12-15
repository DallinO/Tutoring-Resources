using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Abstraction
{
    internal class Comment
    {
        public string _commentor;
        public string _comment;

        public Comment(string commentor, string comment)
        {
            _commentor = commentor;
            _comment = comment;
        }

        public void DisplayComment()
        {
            Console.WriteLine($"\tCommentor: {_commentor}");
            Console.WriteLine($"\tComment: {_comment}");
        }
    }
}
