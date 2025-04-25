# Prime Factors Learning App

An educational application that helps students learn prime factorization through a constructivist approach. The app allows students to explore mathematical concepts like prime numbers and divisibility through interactive trial division.

## Learning Objectives

The app supports Common Core State Standards for 5th grade mathematics:
- CCSS.MATH.CONTENT.5.NBT.B.6: Find whole-number quotients of whole numbers
- CCSS.MATH.CONTENT.5.NF.B.4: Apply and extend previous understandings of multiplication

Students will:
- Explore prime numbers through trial division
- Understand the concept of factors and multiples
- Learn to break down numbers into their prime factors
- Develop number sense and mathematical reasoning
- Build confidence through interactive exploration

## Target Audience

- Grade Level: 5th Grade
- Age Range: 10-11 years
- Prerequisites: Basic multiplication and division skills
- Learning Style: Interactive, exploratory

## Architecture

The application follows a layered architecture:

1. **Presentation Layer**
   - HTML/JavaScript frontend
   - Interactive UI for trial division
   - Visual representation of factor trees
   - Real-time feedback on division attempts

2. **Pedagogy Layer**
   - Tracks student progress
   - Provides hints and guidance
   - Adapts difficulty based on student performance
   - Plans to include personalized learning paths

3. **Core Logic Layer**
   - Pure mathematical functions
   - Integer validation
   - Divisibility checking
   - Prime factorization algorithms

4. **Persistence Layer** (Future)
   - Student progress tracking
   - Performance analytics
   - Learning pattern analysis
   - Personalized recommendations

## Project Structure

```
prime_factors/
├── app/
│   ├── api/           # RESTful API endpoints
│   ├── core/          # Core mathematical logic
│   ├── pedagogy/      # Learning state tracking
│   ├── static/        # Static files (CSS, JS)
│   ├── templates/     # HTML templates
│   └── main.py        # Application entry point
├── docs/              # Documentation
│   ├── testing.md     # Testing guide
│   └── todo.md        # Future improvements
├── tests/             # Test files
├── requirements.txt   # Python dependencies
├── README.md         # This file
└── .env              # Environment variables
```

## Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Adjust values as needed

## Development

- Follow PEP 8 style guide
- Write tests for new features
- Update documentation as needed
- Use meaningful commit messages

## Documentation

- [Testing Guide](docs/testing.md)
- [Future Improvements](docs/todo.md)

## License

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0). This license ensures that:
- The software remains free and open source
- Any modifications must also be open source
- It's suitable for educational use
- It prevents commercial exploitation

See the [LICENSE](LICENSE) file for details.
