# TODO: Future Improvements

## Core Logic
- [ ] Implement core division functions:
  - `is_divisible(dividend, divisor) -> tuple[bool, str]`
    - Pure function for divisibility checking
    - Returns (is_divisible, error_message)
  - `get_quotient(dividend, divisor) -> tuple[float, str]`
    - Returns (quotient, error_message)
  - `get_remainder(dividend, divisor) -> tuple[float, str]`
    - Returns (remainder, error_message)
  - All functions should have:
    - Comprehensive test coverage
    - Clear error messages
    - Input validation
    - Proper documentation

## API Design
- [ ] Design single endpoint for division operations:
  - Accept dividend and divisor
  - Return all necessary information in one response:
    ```json
    {
      "is_divisible": true,
      "quotient": 5,
      "remainder": 0,
      "error": null
    }
    ```
  - Handle all error cases
  - Document API response format

## Documentation
- [ ] Add CONTRIBUTING.md with:
  - Development environment setup
  - Testing procedures
  - Code style guidelines
  - Pull request process
- [ ] Add CHANGELOG.md to track:
  - Version history
  - Feature additions
  - Bug fixes
  - Breaking changes
- [ ] Add CODE_OF_CONDUCT.md for:
  - Community guidelines
  - Expected behavior
  - Reporting procedures
- [ ] Add SECURITY.md for:
  - Security policy
  - Vulnerability reporting
  - Update procedures

## Version Planning

### v0.1 (Day 1)
- Basic prime factorization functionality
- Simple web interface
- Core validation and divisibility checks
- Basic error handling
- Unit tests for core functionality

### v0.2 (Day 2)
- Visual factor tree representation
- Real-time feedback on division attempts
- Basic progress tracking
- Simple error messages
- Additional unit tests

### v0.3 (Day 3)
- Basic hints system
- Student progress persistence
- Simple analytics
- Enhanced error handling
- Integration tests

### v1.0
- Data-driven hints based on student performance
- Improved analytics
- Enhanced UI/UX
- Comprehensive test coverage
- Documentation

### v2.0
- LLM-powered customized hints
- Advanced progress tracking
- Personalized learning paths
- Performance analytics
- Teacher dashboard

### v3.0
- Custom sequencing based on student needs
- Advanced analytics
- Class management features
- Integration with learning management systems
- Mobile-responsive design

### v4.0
- Touch-friendly interface
- Advanced personalization
- AI-driven learning paths
- Comprehensive teacher tools
- API for third-party integration

## Consider Pydantic for Validation

### When to Add Pydantic
- When the API grows to include multiple endpoints with complex data structures
- When you need to validate nested JSON objects
- When you want automatic API documentation (OpenAPI/Swagger)
- When you need to serialize/deserialize data between different formats
- When you want to add more complex validation rules (e.g., regex patterns, custom validators)

### Benefits of Pydantic
1. **Type Safety**: Automatic type checking and conversion
2. **Schema Validation**: Built-in validation for complex data structures
3. **Documentation**: Automatic generation of API documentation
4. **Performance**: Fast validation and serialization
5. **IDE Support**: Better code completion and type hints

### Example of Pydantic Model
```python
from pydantic import BaseModel, Field

class NumberInput(BaseModel):
    value: int = Field(ge=0, lt=100)  # greater than or equal to 0, less than 100
    name: str = Field(min_length=1)
    
    class Config:
        json_schema_extra = {
            "example": {
                "value": 42,
                "name": "test_number"
            }
        }
```

### Current Approach vs Pydantic
Current:
- Simple, pure functions
- Easy to understand and maintain
- Good for learning fundamentals
- Sufficient for basic validation needs

Pydantic:
- More powerful validation features
- Better for complex APIs
- Requires more setup and learning
- Better for production-grade applications

### Migration Strategy
1. Keep current validation functions
2. Add Pydantic models for new endpoints
3. Gradually migrate existing endpoints
4. Use both approaches during transition 